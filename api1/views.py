from rest_framework.response import Response
from rest_framework.decorators import api_view
from second_app.models import Product
from.app2serializers import ProductSerializer


@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serialised = ProductSerializer(products, many=True)
    return Response(serialised.data)

@api_view(['POST'])
def addProduct(request):
    serialised = ProductSerializer(data=request.data)
    if serialised.is_valid():
        serialised.save()
    return Response()
