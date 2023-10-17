from second_app.models import Product
from  rest_framework import serializers


class ProductsSeriaiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'