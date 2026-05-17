from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """A personal note belonging to a user."""

    CATEGORY_CHOICES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('study', 'Study'),
        ('ideas', 'Ideas'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default='')
    tags = models.CharField(max_length=500, blank=True, default='',
                            help_text='Comma-separated tags, e.g. python,django')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,
                                default='personal')
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-updated_at']

    def __str__(self):
        return f'{self.title} — {self.user.username}'

    def tags_list(self):
        """Return tags as a Python list."""
        return [t.strip() for t in self.tags.split(',') if t.strip()]
