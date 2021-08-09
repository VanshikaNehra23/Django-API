from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, DeliverySerializer
from .models import Orders, BoyDetails

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        "Add Order":"/add-order/",
        "Get Details of Orders":"get-order/",
        "Add Details of Delivery Boy":"/add-details/",
        "Get Details of Delivery Boy":"get-details/",
        "Update Any Order" : "update-details/<str:name>/"
    }
    return Response(api_urls)


@api_view(['POST'])
def add_details(request):
    serializer = DeliverySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def add_order(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"order":"declined! Choose a valid delivery boy"})
    # serializer = OrderSerializer(data = request.data)
    # if serializer.is_valid():
    #     x=request.POST.get('deliveryboy')
    #     print(x)
    #     obj = BoyDetails.objects.filter(id=x)
    #     obj.boystatus= obj.boystatus+1
    #     print(obj.boystatus)
    #     obj.save()
    #     print(obj.boystatus)
    #     serializer.save()
    # return Response(serializer.data)


@api_view(['GET'])
def get_details(request):
    boys = BoyDetails.objects.all()
    serializer = DeliverySerializer(boys,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_order(request):
    orders = Orders.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def update_order(request,name):
    details = Orders.objects.get(ordername=name)
    serializer = OrderSerializer(instance=details,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"update":"declined!"})

@api_view(['GET'])
def show(request):
    orderstatus=request.GET.get('orderstatus')
    deliveryboy = request.GET.get('deliveryboy')
    details= Orders.objects.all()
    if orderstatus:
        details = details.filter(orderstatus = orderstatus)
    if deliveryboy:
        details = details.filter(deliveryboy = deliveryboy)
    
    serializer = OrderSerializer(details, many=True)
    return Response(serializer.data)
