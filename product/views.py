from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins
from .models import Product, Category
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductSerializer, CategorySerializer


class ProductListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "id"
    serializer_class = ProductSerializer

    def get_queryset(self):
        items = Product.objects.all()
        query = self.request.GET.get("q")
        qs = (Q(name__icontains=query))

        if query is not None:
            items = items.filter(qs).distinct()
        return items

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class CategoryListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "id"
    serializer_class = CategorySerializer

    def get_queryset(self):
        items = Category.objects.all()
        query = self.request.GET.get("q")
        qs = (Q(name__icontains=query))

        if query is not None:
            items = items.filter(qs).distinct()
        return items

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()