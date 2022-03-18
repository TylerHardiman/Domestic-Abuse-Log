from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Survivor
from .serializers import SurvivorSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_survivors(request):
    cars = Survivor.objects.all()
    serializer = SurvivorSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Survivor_victim(request):
    print(
        'Survivor ', f"{request.Survivor.id} {request.Survivor.email} {request.Survivor.Survivorname}")
    if request.method == 'POST':
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Survivor=request.Survivor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cars = Survivor.objects.filter(Survivor_id=request.Survivor.id)
        serializer = SurvivorSerializer(cars, many=True)
        return Response(serializer.data)
