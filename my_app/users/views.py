
import facebook
from datetime import datetime

from rest_framework import status
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from common.paginations import MyCustomPagination

from .authentication import JWTAuthentication, create_jwt, jwt_payload_handler_custom
from .models import User
from .permissions import UserPermissions
from .serializers import UserSerializer


jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    User endpoint permissions:
     - retrieve: user authenticated
     - update: itself user authenticated
    """
    lookup_field = 'pk'

    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = (JWTAuthentication,)
    pagination_class = MyCustomPagination
    permission_classes = (UserPermissions,)

    ''' *** TO DO ***
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        token = create_jwt(serializer.instance)
        
        return Response({'token': token}, status=status.HTTP_201_CREATED, headers=headers)
    '''


class ObtainJWTokenCustom(APIView):

    def post(self, request, *args, **kwargs):
        provider = self.request.data.get('provider')

        if provider == 'facebook':
            fb_token = self.request.data.get('token')

            try:
                graph = facebook.GraphAPI(access_token=fb_token)
                user_info = graph.get_object(
                    id='me',
                    fields='id, first_name, middle_name, last_name, '
                           'birthday, gender, email, picture, location'
                )
                user_info['provider_id'] = user_info.get('id')
                user_info['names'] = user_info.get('first_name')
                user_info['surnames'] = '{0} {1}'.format(user_info.get('middle_name'), user_info.get('last_name'))
                user_info['picture'] = user_info['picture']['data']['url']
                user_info['location'] = user_info['location']['name']
                user_info['last_login'] = str(datetime.now())

            except facebook.GraphAPIError as exception:
                # TO DO: Add logger here adding the graph error.
                print(exception.message)
                return Response(exception.message, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            try:
                status_response = status.HTTP_200_OK
                user = User.objects.get(provider_id=user_info.get('id'))

                if not user.is_active:
                    Response('User account is disabled.', status=status.HTTP_400_BAD_REQUEST)

                serializer = UserSerializer(user, data=user_info)

            except User.DoesNotExist:
                status_response = status.HTTP_201_CREATED

                serializer = UserSerializer(data=user_info)

            if not serializer.is_valid():
                Response(data=serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)

            serializer.save()
            payload = jwt_payload_handler_custom(serializer.instance)

            return Response({'token': jwt_encode_handler(payload)}, status=status_response)

        return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)