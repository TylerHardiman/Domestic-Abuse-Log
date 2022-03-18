from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
<<<<<<< Updated upstream:backend/drf_jwt_backend/abuselog/views.py
from .serializers import UserSerializer
=======
from .models import Survivor
from .serializers import SurvivorSerializer

>>>>>>> Stashed changes:backend/drf_jwt_backend/records/views.py
# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
<<<<<<< Updated upstream:backend/drf_jwt_backend/abuselog/views.py
def get_all_users(request):
    User = User.objects.all()
    serializer = UserSerializer(User, many=True)
=======
def get_all_cars(request):
    cars = Survivor.objects.all()
    serializer = SurvivorSerializer(cars, many=True)
>>>>>>> Stashed changes:backend/drf_jwt_backend/records/views.py
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_victim(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
<<<<<<< Updated upstream:backend/drf_jwt_backend/abuselog/views.py
        serializer = UserSerializer(data=request.data)
=======
        serializer = SurvivorSerializer(data=request.data)
>>>>>>> Stashed changes:backend/drf_jwt_backend/records/views.py
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
<<<<<<< Updated upstream:backend/drf_jwt_backend/abuselog/views.py
        User = User.objects.filter(user_id=request.user.id)
        serializer = UserSerializer(User, many=True)
=======
        cars = Survivor.objects.filter(user_id=request.user.id)
        serializer = SurvivorSerializer(cars, many=True)
>>>>>>> Stashed changes:backend/drf_jwt_backend/records/views.py
        return Response(serializer.data)
