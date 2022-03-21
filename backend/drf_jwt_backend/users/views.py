from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import AbuseLog, User
from .serializers import AbuseLogSerializer, UserSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_users(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.first_name} {request.user.first_name}")
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.filter(user_id=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_abuselog(request):
    abuselogs = AbuseLog.objects.all()
    serializer = AbuseLogSerializer(abuselogs, many=True)
    return Response(serializer.data)
    
api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_abuselog(request):
    print(
        'User ', f"{request.user.id} {request.user.post} {request.user.name} {request.user.email} {request.user.body} {request.user.created_on} {request.user.active}")
    if request.method == 'POST':
        serializer = AbuseLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        abuselogs = AbuseLog.objects.filter(user_id=request.user.id)
        serializer = AbuseLogSerializer(abuselogs, many=True)
        return Response(serializer.data)

