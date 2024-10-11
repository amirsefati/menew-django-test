from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerialize
from drf_yasg.utils import swagger_auto_schema
from .models import User

class UserCreateView(APIView):

    @swagger_auto_schema(
        request_body=UserSerialize,
        responses={201: UserSerialize(), 400: 'Bad Request'},
        operation_description="Create a user"
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerialize(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            email = validated_data.get('email')
            password = validated_data.get('password')

            #I use stackoverflow to find this line
            extra_fields = {k: v for k, v in validated_data.items() if k not in [
                'email', 'password']}
            user = User.objects.create_user(
                email=email, password=password, **extra_fields)
            response_serializer = UserSerialize(user)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
