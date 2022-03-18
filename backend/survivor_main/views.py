from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


from .models import Survivor
from .models import AbuseLog
from serializers import SurvivorSerializer, AbuseLogSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_survivors(request):
    Survivor = Survivor.objects.all()
    serializer = SurvivorSerializer(Survivor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_abuselog(request):
    AbuseLog = AbuseLog.objects.all()
    serializer = AbuseLogSerializer(AbuseLog, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def survivor_victim(request):
    print(
        'Survivor ', f"{request.Survivor.id} {request.Survivor.email} {request.Survivor.first_name} {request.Survivor.last_name}")
    if request.method == 'POST':
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Survivor=request.Survivor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        survivors = Survivor.objects.filter(Survivor_id=request.Survivor.id)
        serializer = SurvivorSerializer(survivors, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def survivor_log(request):
    print(
        'AbuseLog ', f"{request.AbuseLog.id} {request.AbuseLog.post} {request.AbuseLog.name} {request.AbuseLog.email} {request.AbuseLog.body} {request.AbuseLog.created_on} {request.AbuseLog.active}")
    if request.method == 'POST':
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(AbuseLog=request.AbuseLog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        AbuseLog = AbuseLog.objects.filter(AbuseLog_id=request.AbuseLogid)
        serializer = AbuseLogSerializer(AbuseLog, many=True)
        return Response(serializer.data)
