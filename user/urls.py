from django.urls import path
from .views import UserCreateView, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create-user/', UserCreateView.as_view(), name='create-user'),
    path('', UserListView.as_view(), name='user-list'),
    path('<str:id>/', UserUpdateView.as_view(),
         name='user-update'),
    path('<str:id>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
