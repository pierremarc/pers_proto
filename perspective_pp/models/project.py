from django.contrib.gis.db import models as m
from django.contrib.auth.models import User

class Project(m.Model):
    id = m.AutoField(primary_key=True)
    created_at = m.DateTimeField(auto_now_add=True)

# << references

class Workflow(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name



class WorkflowItem(m.Model):
    id = m.AutoField(primary_key=True)
    process = m.ForeignKey(Workflow, m.CASCADE)
    name = m.CharField(max_length=64)
    index = m.IntegerField()

    def __str__(self):
        return self.name

class ContactRef(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name

class KindRef(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name


class TypeRef(m.Model):
    id = m.AutoField(primary_key=True)
    kind = m.ForeignKey(KindRef, m.CASCADE)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name

class ProgramRef(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name

class ProcessRef(m.Model):
    id = m.AutoField(primary_key=True)
    name = m.CharField(max_length=64)

    def __str__(self):
        return self.name



# >> references



class EventLog(m.Model):
    id = m.AutoField(primary_key=True)
    created_at = m.DateTimeField(auto_now_add=True)
    model = m.CharField(max_length=64)
    action = m.CharField(max_length=64)
    