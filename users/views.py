from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer

class RequestAccountView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            if not user.is_active:
                return Response({"error": "Account pending admin approval."}, status=status.HTTP_403_FORBIDDEN)
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'name': f"{user.first_name} {user.last_name}",
                    'role': user.role
                }
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)