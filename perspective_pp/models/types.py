from django.contrib.gis.db import models as m
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ranges

from .project import (
    Project,
    ContactRef,
    TypeRef,
    ProgramRef,
    ProcessRef, 
    )



class T(m.Model):
    class Meta:
        abstract = True

    id = m.AutoField(primary_key=True)
    parent = m.ForeignKey(T, on_delete=m.CASCADE, null=True, blank=True)
    project = m.ForeignKey(Project, on_delete=m.CASCADE)
    created_at = m.DateTimeField(auto_now_add=True)
    user = m.ForeignKey(User, on_delete=m.CASCADE)

    def __str__(self):
        return '{}({}) {}'.format(self._meta.verbose_name, self.pid.id, self.value)


## geometry
class Point(T):
    value = m.PointField(srid=4326)

class Polygon(T):
    value = m.PolygonField(srid=4326)


## strat & conn
class ProjectName(T):
    value = m.CharField(max_length=128)

class SiteName(T):
    value = m.CharField(max_length=128)

class Occupying(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Exploiting(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Developer(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Intent(T):
    value = m.TextField()

class PresentState(T):
    value = m.TextField()

class ProjectedState(T):
    value = m.TextField()


class HorizonDesign(T):
    value = m.DateTimeField()

class HorizonBuild(T):
    value = m.DateTimeField()

class HorizonInstall(T):
    value = m.DateTimeField()

class Contact(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)
 

## bma

class Year(T):
    value = m.IntegerField()

class InOut(T):
    A = 'i'
    B = 'o'
    CHOICES = (
        (A, 'In'),
        (B, 'Out'),
    )
    value = m.CharField(max_length=1, choices=CHOICES)

class PubPriv(T):
    A = 'u'
    B = 'r'
    CHOICES = (
        (A, 'Public'),
        (B, 'Private'),
    )
    value = m.CharField(max_length=1, choices=CHOICES)

class Rdb(T):
    A = 'n'
    B = 'j'
    C = 'g'
    CHOICES = (
        (A, 'No'),
        (B, 'Ju'),
        (C, 'Ge'),
    )
    value = m.CharField(max_length=1, choices=CHOICES)


class ProjectType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class MoGo(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Program(T):
    value = m.ForeignKey(ProgramRef, on_delete=m.CASCADE)

class Description(T):
    value = m.TextField()

class Manager(T):
    value = m.ForeignKey(User, on_delete=m.CASCADE)

class Process(T):
    value = m.ForeignKey(ProcessRef, on_delete=m.CASCADE)

class FeeType(T):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    CHOICES = (
        (A, 'Fixe'),
        (B, 'Mixte'),
        (C, 'Fixe forfait'),
        (D, 'Fourchette forfait'),
    )
    value = m.CharField(max_length=1, choices=CHOICES)

class FeeRate(T):
    value = ranges.NumericRange()

class StudyFee(T):
    value = m.FloatField()

class Fee(T):
    value = m.FloatField()
    
class News(T):
    value = m.BooleanField()

class BmaAvis(T):
    value = m.DateField()

class BmaCand(T):
    value = m.DateField()

class BmaOffre(T):
    value = m.DateField()

class BmaComite(T):
    value = m.DateField()

class BmaCandidat(T):
    value = m.IntegerField()

class BmaSoumis(T):
    value = m.IntegerField()

class BmaDefr(T):
    value = m.IntegerField()

class Expert(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Tenderer(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

class Winner(T):
    value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)


## logement 





## ecole


## draft

class Nova(T):
    value = m.IntegerField()

# class ProjectType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class BuildingType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class HousingType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class SpaceType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class InfraType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class PlanningType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

class InterventionType(T):
    value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)


