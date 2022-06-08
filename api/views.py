
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from base.models import Item


@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def singleData(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateItem(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=items, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteItem(request, pk):
    items = Item.objects.get(id=pk)
    items.delete()
    return Response("item deleted")

