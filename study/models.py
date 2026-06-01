from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


class Segment(models.Model):
    chapter = models.PositiveIntegerField(default=1)
    position = models.PositiveIntegerField(unique=True)
    text_it = models.CharField(max_length=160)
    translation_pt = models.CharField(max_length=180)
    verb = models.CharField(max_length=60, blank=True)
    present_example = models.CharField(max_length=180, blank=True)
    past_example = models.CharField(max_length=180, blank=True)
    future_example = models.CharField(max_length=180, blank=True)
    context_note = models.CharField(max_length=180, blank=True)
    source_paragraph = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.position:03d} - {self.text_it}"


class ReviewState(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    segment = models.ForeignKey(
        Segment,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    due_at = models.DateTimeField(default=timezone.now)
    interval_days = models.FloatField(default=0)
    ease_factor = models.FloatField(default=2.5)
    repetitions = models.PositiveIntegerField(default=0)
    lapses = models.PositiveIntegerField(default=0)
    last_grade = models.CharField(max_length=12, blank=True)
    first_seen_at = models.DateTimeField(null=True, blank=True)
    learned_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["segment__position"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "segment"],
                name="unique_review_state_per_user_segment",
            )
        ]

    @property
    def is_learned(self):
        return self.learned_at is not None

    def mark_seen(self):
        if self.first_seen_at is None:
            self.first_seen_at = timezone.now()
            self.save(update_fields=["first_seen_at", "updated_at"])

    def apply_grade(self, grade):
        now = timezone.now()
        self.last_grade = grade

        if grade == "again":
            self.lapses += 1
            self.repetitions = 0
            self.interval_days = 0
            self.ease_factor = max(1.3, self.ease_factor - 0.2)
            self.due_at = now + timedelta(minutes=10)
            self.save()
            return

        if grade == "hard":
            self.repetitions += 1
            self.interval_days = max(1, self.interval_days * 1.2)
            self.ease_factor = max(1.3, self.ease_factor - 0.05)
        elif grade == "good":
            self.repetitions += 1
            if self.interval_days == 0:
                self.interval_days = 3
            else:
                self.interval_days = max(2, self.interval_days * self.ease_factor)
        elif grade == "easy":
            self.repetitions += 1
            self.ease_factor += 0.15
            if self.interval_days == 0:
                self.interval_days = 5
            else:
                self.interval_days = max(4, self.interval_days * self.ease_factor * 1.3)

        if self.learned_at is None and grade in {"hard", "good", "easy"}:
            self.learned_at = now

        self.due_at = now + timedelta(days=self.interval_days)
        self.save()
