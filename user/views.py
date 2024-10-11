from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerialize
from drf_yasg.utils import swagger_auto_schema
from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class UserCreateView(APIView):
    permission_classes = [IsAdminUser]

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

            # I use stackoverflow to find this line
            extra_fields = {k: v for k, v in validated_data.items() if k not in [
                'email', 'password']}
            user = User.objects.create_user(
                email=email, password=password, **extra_fields)
            response_serializer = UserSerialize(user)

            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialize
    permission_classes = [IsAdminUser]


class UserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerialize
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
