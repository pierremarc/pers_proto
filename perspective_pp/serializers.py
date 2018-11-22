from rest_framework import serializers
from .models import *

class Ser(serializers.ModelSerializer):
    pass

# Serializers define the API representation.
class ProjectSerializer(Ser):
    class Meta:
        model = Project
        fields =(
            'starttime_set',
            'endtime_set',
            'name_set',
            'note_set',
            # 'point_set',
            # 'polygon_set',
            'step_set',
            )
        depth = 1



class ProcessSerializer(Ser):
    class Meta:
        model = Process
        fields = ('id', 'name', 'processitem_set')

class ProcessItemSerializer(Ser):
    class Meta:
        model = ProcessItem
        fields = '__all__'



class UserSerializer(Ser):
    class Meta:
        model = User
        fields = ('id', 'username')