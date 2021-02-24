from rest_framework import viewsets
from . import models
from . import serializers

class ItemViewset(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer