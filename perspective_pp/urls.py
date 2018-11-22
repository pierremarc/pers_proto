from django.urls import path, include
from rest_framework import routers

from .models import *
from .views import (
    reg_type,
    ProjectViewSet,
    ProcessViewSet,
    ProcessItemViewSet,
    UserViewSet,
    get_project_point,
    get_project_polygon,
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('project', ProjectViewSet)

router.register('ref/process', ProcessViewSet)
router.register('ref/processitem', ProcessItemViewSet)
router.register('ref/user', UserViewSet)

reg_type(router, StartTime)
reg_type(router, EndTime)
reg_type(router, Name)
reg_type(router, Note)
reg_type(router, Point)
reg_type(router, Polygon)
reg_type(router, Step)

urlpatterns = [
    path('data/', include(router.urls)),
    path('layer/point', get_project_point, name='pers-layer-points'),
    path('layer/polygon', get_project_polygon, name='pers-layer-polygons'),
]
