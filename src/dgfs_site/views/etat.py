from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions, status


from rest_framework import generics, mixins
import datetime,random, string

from dgfs_site.models import Etat
from dgfs_site.serializers import EtatSerializer


class EtatMixinsViews(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin):
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

    def perform_create(self, serializer):
        etatNom = serializer.validated_data.get('etatNom')
        if not etatNom:
            raise exceptions.ValidationError("etatNom field is required")
        etatDesc = serializer.validated_data.get('etatDesc') or None
        if etatDesc is None:
            etatDesc = etatNom
        serializer.save(etatDesc=etatDesc)
        return Response({'message': 'Creation avec succes'}, status=201)

    def perform_update(self, serializer):
        etatNom = serializer.validated_data.get('etatNom')
        if not etatNom:
            raise exceptions.ValidationError("etatNom field is required")
        etatDesc = serializer.validated_data.get('etatDesc') or None
        if etatDesc is None:
            etatDesc = etatNom
        serializer.save(etatDesc=etatDesc)
        return Response({'message': 'Mise a Jour avec succes'}, status=200)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('etatID')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({"message": "Suppression avec succes"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)
        return Response({"message": "Mise a jour avec succes"})

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return Response({"message": "Mise a jour avec succes"})
