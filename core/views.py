from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import *
from rest_framework.permissions import AllowAny
from .response import CustomResponse


class UserLoginViewSet(viewsets.ViewSet):
    serializer_class = AdminLoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        response = CustomResponse()
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            
            # Authenticate the user
            user = authenticate(username=email, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    response.successResponse("Login successful", {"token": token.key}),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    response.errorResponse("Invalid email or password"),
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
