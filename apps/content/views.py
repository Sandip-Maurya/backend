"""
Views for content app.
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import SustainableGiftingItem
from .serializers import SustainableGiftingItemSerializer


@extend_schema(
    tags=['Content'],
    summary='List sustainable gifting items',
    description='Get all active sustainable gifting items ordered by order field',
    responses={200: SustainableGiftingItemSerializer(many=True)},
)
@api_view(['GET'])
@permission_classes([AllowAny])
def sustainable_gifting_list_view(request):
    """Get all active sustainable gifting items."""
    queryset = SustainableGiftingItem.objects.filter(is_active=True).order_by('order')
    serializer = SustainableGiftingItemSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

