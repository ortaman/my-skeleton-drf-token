
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

from .views import UserViewSet


urlpatterns = [
    path('token-auth/', obtain_auth_token, name='token_auth'),

    path('user/', UserViewSet.as_view({'post': 'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put':'update'})),
]
