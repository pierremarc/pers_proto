from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError, HttpResponseForbidden
from django.core.serializers import serialize
from rest_framework import viewsets, serializers

from .serializers import *
from .models import *


# ViewSets define the view behavior.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer


class ProcessItemViewSet(viewsets.ModelViewSet):
    queryset = ProcessItem.objects.all()
    serializer_class = ProcessItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def reg_type(router, M):
    model_name = M._meta.model_name

    class S(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = M
            fields = ('id', 'value', 'user', 'pid', 'created_at', 'updated_at')

        def create(self, validated_data):
            request = self.context['request']
            user = request.user
            value = validated_data.get('value')
            pid = validated_data.get('pid')
            return M.objects.create(
                user=user,
                value=value,
                pid=pid,
            )

    class V(viewsets.ModelViewSet):
        queryset = M.objects.all()
        serializer_class = S

    router.register('typ/{}'.format(model_name), V)


class GeoAcc:
    def __init__(self, geom_type):
        self.features = []
        self.geom_type = geom_type

    def push(self, coords, props):
        self.features.append(
            dict(
                type='Feature',
                geometry=dict(type=self.geom_type, coordinates=coords),
                properties=props))

    def geojson(self):
        return dict(type="FeatureCollection", features=self.features)


def get_project_point(request):
    geo_acc = GeoAcc("Point")
    for p in Point.objects.all():
        project_ser = ProjectSerializer(
            instance=p.pid, context={'request': request})
        geo_acc.push(p.value.coords, dict(project=project_ser.data))

    return JsonResponse(geo_acc.geojson())

def get_project_polygon(request):
    geo_acc = GeoAcc("Polygon")
    for p in Polygon.objects.all():
        project_ser = ProjectSerializer(
            instance=p.pid, context={'request': request})
        geo_acc.push(p.value.coords, dict(project=project_ser.data))

    return JsonResponse(geo_acc.geojson())
