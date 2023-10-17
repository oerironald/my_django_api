from rest_framework.response import Response
from rest_framework.decorators import api_view
from second_app.models import Product
from .api3serializers import ProductsSeriaiser


@api_view(['GET'])
def getdata(request):
    products = Product.objects.all()
    serialized = ProductsSeriaiser(products, many=True)
    return Response(serialized.data)