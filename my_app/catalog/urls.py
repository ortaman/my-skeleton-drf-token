
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from .views import CategoryViewSet, SkillViewSet


urlpatterns = [
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('skills/', SkillViewSet.as_view({'get': 'list'}))
]
