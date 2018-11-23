from rest_framework import serializers
from .models.project import *

from .models.types import TYPES


class Ser(serializers.ModelSerializer):
    pass


# class Ser(serializers.HyperlinkedModelSerializer):
#     pass

project_fields = ['{}_set'.format(T._meta.model_name) for _, T in TYPES]
project_fields.append('id')


class ProjectSerializer(Ser):
    class Meta:
        model = Project
        fields = project_fields
        depth = 1


def make_computed_latest(field_name):
    set_name = '{}_set'.format(field_name)

    def inner(self, instance):
        f_set = getattr(instance, set_name)
        try:
            return f_set.first().value
        except Exception:
            return None

    return inner


def project_ser(field_names):

    # meta = type('Meta', (),
    #             dict(model=Project, depth=1, fields=['id'] + field_names))
    attrs = dict(
        # Meta=meta,
        id=serializers.IntegerField(read_only=True), )

    for field_name in field_names:
        getter_name = 'get_{}'.format(field_name)
        attrs[field_name] = serializers.SerializerMethodField(read_only=True)
        attrs[getter_name] = make_computed_latest(field_name)

    ser = type('ProjectSerializer', (serializers.Serializer, ), attrs)

    return ser


class WorkflowSerializer(Ser):
    class Meta:
        model = Workflow
        fields = ('id', 'name', 'workflowitem_set')


class WorkflowItemSerializer(Ser):
    class Meta:
        model = WorkflowItem
        fields = '__all__'


class UserSerializer(Ser):
    class Meta:
        model = User
        fields = ('id', 'username')


class ContactSerializer(Ser):
    class Meta:
        model = ContactRef
        fields = ('id', 'name')