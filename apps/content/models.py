"""
Content models for Dolce Fiore.
"""
import uuid
from django.db import models


class SustainableGiftingItem(models.Model):
    """Model for Sustainable Gifting section items on home page."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'sustainable_gifting_items'
        ordering = ['order', 'created_at']
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['order']),
        ]
    
    def __str__(self):
        return self.title

