from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated

import datetime,random, string

from .models import Province
from .authentication import create_access_token, create_refresh_token , JWTAuthentication, decode_refresh_token
from .serializers import ProvinceSerializer


class ProvinceMixinsViews(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('provinceNom')
        content = serializer.validated_data.get('provinceDesc') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def perform_update(self, serializer):
        name = serializer.validated_data.get('provinceNom')
        content = serializer.validated_data.get('provinceDesc') or None
        if content is None:
            content = name
        serializer.save(content=content)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('provinceID')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
