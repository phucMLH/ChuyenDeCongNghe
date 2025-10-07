from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.utils import timezone

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemSerializer
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created']

    # Cache the list view for 60 seconds as an example
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        # Call the parent to get the normal response
        response = super().list(request, *args, **kwargs)
        # Attach a debug header indicating when this response was generated.
        # This header will be cached together with the response, so it helps
        # determine whether subsequent requests returned a cached response.
        response['X-Cached-At'] = timezone.now().isoformat()
        return response
