
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin

from common.paginations import MyCustomPagination
from common.utils import create_jwt
from .models import User
from .serializers import UserSerializer
from .permissions import UserPermissions


class UserViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    User endpoint permissions:
     - create: alloy any
     - retrieve: admin or user authenticated
     - update: itself user authenticated
    """
    lookup_field = 'pk'

    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = MyCustomPagination
    permission_classes = (UserPermissions,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        token = create_jwt(serializer.instance)
        
        return Response({'token': token}, status=status.HTTP_201_CREATED, headers=headers)

    '''
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsUserOrAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsSelfUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        pass
    '''
