
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from users.authentication import JWTAuthentication
from .models import Category, Skill
from .serializers import CategorySerializer, SkillSerializer


class CategoryViewSet(ListModelMixin, GenericViewSet):
    """
    User endpoint permissions:
     - list: user authenticated
    """
    lookup_field = 'pk'

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    authentication_classes = (JWTAuthentication,)
    pagination_class = None


class SkillViewSet(ListModelMixin, GenericViewSet):
    """
    User endpoint permissions:
     - list: user authenticated
    """
    lookup_field = 'pk'

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    authentication_classes = (JWTAuthentication,)
    pagination_class = None
