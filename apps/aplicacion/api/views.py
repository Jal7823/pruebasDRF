from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Cars
from .serializer import CarsSerializer

@api_view(['GET', 'POST'])
def cars_api_view(request):

    if request.method == 'GET':
        cars = Cars.objects.all()
        cars_serializer = CarsSerializer(cars,many=True)
        return Response(cars_serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save()
            return Response(CarsSerializer(car).data,status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def car_api_view(request,pk):
    car = Cars.objects.filter(id=pk).first()

    if car:

        if request.method == 'GET':
            car = CarsSerializer(car)
            return Response(car.data,status=status.HTTP_200_OK)

        if request.method == 'PUT':
            car_serializer = CarsSerializer(car,data = request.data)
            if car_serializer.is_valid():
                car_serializer.save()
                return Response(car_serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(car_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            car.delete()
            return Response({'mssage':f'the resource {car.name} was deleted '},status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'message':'resource not found'},status=status.HTTP_404_NOT_FOUND)