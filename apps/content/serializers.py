"""
Serializers for content app.
"""
from rest_framework import serializers
from .models import SustainableGiftingItem


class SustainableGiftingItemSerializer(serializers.ModelSerializer):
    """Serializer for sustainable gifting items."""
    
    class Meta:
        model = SustainableGiftingItem
        fields = [
            'id',
            'title',
            'description',
            'image_url',
            'order',
            'is_active',
        ]

