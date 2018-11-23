from django.urls import path, include
from rest_framework import routers

from .views import (get_project_point, get_project_polygon, reg_type,
                    ProjectViewSet, UserViewSet, ContactViewSet)

from .models.types import TYPES

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
router.register('ref/user', UserViewSet)
router.register('ref/contact', ContactViewSet)

for tname, T in TYPES:
    reg_type(router, T)

urlpatterns = [
    path('data/', include(router.urls)),
    path(
        'layer/point/<path:fields>',
        get_project_point,
        name='pers-layer-points'),
    path(
        'layer/polygon/<path:fields>',
        get_project_polygon,
        name='pers-layer-polygons'),
]
