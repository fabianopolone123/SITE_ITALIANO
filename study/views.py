from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import ReviewState, Segment


def ensure_review_states(user):
    existing = set(
        ReviewState.objects.filter(user=user).values_list("segment_id", flat=True)
    )
    missing = Segment.objects.exclude(id__in=existing)
    ReviewState.objects.bulk_create(
        [ReviewState(user=user, segment=segment) for segment in missing],
        ignore_conflicts=True,
    )


def get_next_review(user):
    now = timezone.now()
    due_learned = (
        ReviewState.objects.select_related("segment")
        .filter(user=user, due_at__lte=now, learned_at__isnull=False)
        .order_by("due_at", "segment__position")
        .first()
    )
    if due_learned:
        return due_learned

    return (
        ReviewState.objects.select_related("segment")
        .filter(user=user, due_at__lte=now, learned_at__isnull=True)
        .order_by("segment__position")
        .first()
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("study:dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("study:dashboard")
        messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "study/login.html")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("study:dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not username or not password1:
            messages.error(request, "Preencha usuário e senha.")
        elif password1 != password2:
            messages.error(request, "As senhas precisam ser iguais.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Esse usuário já existe.")
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect("study:dashboard")

    return render(request, "study/signup.html")


def logout_view(request):
    logout(request)
    return redirect("study:login")


@login_required
def dashboard(request):
    ensure_review_states(request.user)
    totals = ReviewState.objects.filter(user=request.user).aggregate(
        all_cards=Count("id"),
        learned=Count("id", filter=Q(learned_at__isnull=False)),
        seen=Count("id", filter=Q(first_seen_at__isnull=False)),
        due=Count(
            "id",
            filter=Q(due_at__lte=timezone.now()) & Q(learned_at__isnull=False),
        ),
    )
    next_review = get_next_review(request.user)
    progress = 0
    if totals["all_cards"]:
        progress = round((totals["seen"] / totals["all_cards"]) * 100)

    return render(
        request,
        "study/dashboard.html",
        {
            "totals": totals,
            "progress": progress,
            "next_segment": next_review.segment if next_review else None,
        },
    )


@login_required
def study_card(request):
    ensure_review_states(request.user)
    review = get_next_review(request.user)
    if review:
        review.mark_seen()
    return render(
        request,
        "study/study_card.html",
        {"segment": review.segment if review else None},
    )


@login_required
@require_POST
def answer_card(request, segment_id):
    ensure_review_states(request.user)
    review = get_object_or_404(
        ReviewState.objects.select_related("segment"),
        user=request.user,
        segment_id=segment_id,
    )
    grade = request.POST.get("grade")
    labels = {
        "again": "Errei: este card volta mais tarde.",
        "hard": "Difícil: card aprendido, revisão marcada.",
        "good": "Bom: card aprendido, revisão marcada.",
        "easy": "Fácil: card aprendido, revisão mais distante.",
    }
    if grade in labels:
        review.apply_grade(grade)
        messages.success(request, labels[grade])
    return redirect("study:study")


@login_required
def read_learned(request):
    ensure_review_states(request.user)
    seen_segments = (
        Segment.objects.filter(
            reviews__user=request.user,
            reviews__first_seen_at__isnull=False,
        )
        .order_by("position")
        .distinct()
    )
    return render(
        request,
        "study/read_learned.html",
        {"segments": seen_segments},
    )
