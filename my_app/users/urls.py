
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from .views import ObtainJWTokenCustom, UserViewSet


urlpatterns = [
    path('token/', ObtainJWTokenCustom.as_view(), name='token'),
    # path('token-refresh/', refresh_jwt_token, name='token_refresh'),
    # path('token-verify/', verify_jwt_token, name='token_verify'),

    path('user/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
