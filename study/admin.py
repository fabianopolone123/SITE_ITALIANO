from django.contrib import admin

from .models import ReviewState, Segment


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ("position", "chapter", "text_it", "translation_pt", "verb")
    list_filter = ("chapter", "verb")
    search_fields = ("text_it", "translation_pt", "verb")


@admin.register(ReviewState)
class ReviewStateAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "segment",
        "due_at",
        "interval_days",
        "ease_factor",
        "repetitions",
        "lapses",
        "first_seen_at",
        "learned_at",
    )
    list_filter = ("learned_at", "last_grade")
