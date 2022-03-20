from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from users.models import AbuseLog, Survivor
from users.serializers import AbuseLogSerializer, SurvivorSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_survivors(request):
    survivors = Survivor.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def survivor_survivors(request):
    print(
        'survivor ', f"{request.survivor.id} {request.survivor.email} {request.survivor.first_name} {request.survivor.first_name}")
    if request.method == 'POST':
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(survivor=request.survivor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        survivors = Survivor.objects.filter(survivor_id=request.survior.id)
        serializer = SurvivorSerializer(survivors, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_abuselog(request):
    abuselog = AbuseLog.objects.all()
    serializer = AbuseLogSerializer(abuselog, many=True)
    return Response(serializer.data)
    
api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def survivor_abuselog(request):
    print(
        'abuselog ', f"{request.abuselog.id} {request.abuselog.post} {request.abuselog.name} {request.abuselog.email} {request.abuselog.body} {request.abuselog.created_on} {request.abuselog.active}")
    if request.method == 'POST':
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(abuselog=request.abuselog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        abuselog = AbuseLog.objects.filter(abuselog_id=request.abuselog.id)
        serializer = AbuseLogSerializer(abuselog, many=True)
        return Response(serializer.data)

