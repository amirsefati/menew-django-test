from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerialize
from drf_yasg.utils import swagger_auto_schema


class UserCreateView(APIView):

    @swagger_auto_schema(
        request_body=UserSerialize,
        responses={201: UserSerialize(), 400: 'Bad Request'},
        operation_description="Create a user profile with a user and bio"
    )
    def post(self, request):
        serializer = UserSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
