"""
Admin configuration for content app.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import SustainableGiftingItem


@admin.register(SustainableGiftingItem)
class SustainableGiftingItemAdmin(admin.ModelAdmin):
    """Admin for sustainable gifting items."""
    list_display = ['title', 'order', 'is_active', 'image_preview', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['order', 'created_at']
    readonly_fields = ['id', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'title', 'description', 'image_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['make_active', 'make_inactive']
    
    def image_preview(self, obj):
        """Display image as thumbnail."""
        if obj.image_url:
            return format_html(
                '<img src="{}" style="max-width: 100px; max-height: 100px; object-fit: cover;" />',
                obj.image_url
            )
        return '-'
    image_preview.short_description = 'Preview'
    
    def make_active(self, request, queryset):
        """Bulk action to mark items as active."""
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} item(s) marked as active.')
    make_active.short_description = 'Mark selected items as active'
    
    def make_inactive(self, request, queryset):
        """Bulk action to mark items as inactive."""
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} item(s) marked as inactive.')
    make_inactive.short_description = 'Mark selected items as inactive'

