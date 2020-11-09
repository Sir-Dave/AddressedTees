from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = ["image", "name", "price"]
        fields = "__all__"


    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This product name has already been used!")

        return value



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = "__all__"

    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This category name has already been used!")

        return value

