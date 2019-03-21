
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin

from common.paginations import MyCustomPagination
from .models import User
from .serializers import UserSerializer
from .permissions import AllowAnyCreateOrIsAuthenticated, IsSelfUserOrReadOnly


class UserViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    Endpoint to create users for anyone, to retrieve and update the user only by the owner.
    """
    lookup_field = 'pk'

    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (JSONWebTokenAuthentication,)
    pagination_class = MyCustomPagination
    permission_classes = (AllowAnyCreateOrIsAuthenticated, IsSelfUserOrReadOnly)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(serializer.instance)
        token = jwt_encode_handler(payload)

        return Response({'token': token}, status=status.HTTP_201_CREATED, headers=headers)

    ''' TODO
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsUserOrAdmin]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsSelfUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullAccountSerializer
        return BasicAccountSerializer
    '''
