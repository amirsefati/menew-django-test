from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('create-profile/', UserCreateView.as_view(), name='create-profile'),
]
