from django.contrib.gis.db import models as m
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ranges

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
    project = m.ForeignKey(Project, on_delete=m.CASCADE)
    created_at = m.DateTimeField(auto_now_add=True)
    user = m.ForeignKey(User, on_delete=m.CASCADE)

    def __str__(self):
        return '{}({}) {}'.format(self._meta.verbose_name, self.project.id, self.value)


TYPES = []

def make_type(name, value, attrs=dict()):
    attrs.update(dict(
        Meta=type( 'Meta', (), dict(app_label='perspective_pp',ordering = ['-created_at']) ),
        __module__='perspective_pp.models.types',
        value = value,
        parent = m.ForeignKey(
            'perspective_pp.{}'.format(name), 
            on_delete=m.CASCADE,
            related_name='+',
            blank=True,
            null=True)
    ))
    cls = type(name, (T,), attrs)

    TYPES.append((name, cls))
    return cls


## geometry
Point = make_type('Point', m.PointField(srid=4326))
Polygon = make_type('Polygon', m.PolygonField(srid=4326))


## strat & conn
ProjectName = make_type('ProjectName', m.CharField(max_length=128))
SiteName = make_type('SiteName',m.CharField(max_length=128))
Occupying = make_type('Occupying',m.ForeignKey(ContactRef, on_delete=m.CASCADE))
Exploiting = make_type('Exploiting',m.ForeignKey(ContactRef, on_delete=m.CASCADE))
Developer = make_type('Developer',m.ForeignKey(ContactRef, on_delete=m.CASCADE))
Intent = make_type('Intent',m.TextField())
PresentState = make_type('PresentState', m.TextField())
ProjectedState = make_type('ProjectedState',m.TextField())
HorizonDesign = make_type('HorizonDesign',m.IntegerField())
HorizonBuild = make_type('HorizonBuild',m.IntegerField())
HorizonInstall = make_type('HorizonInstall',m.DateTimeField())
Contact = make_type('Contact',m.ForeignKey(ContactRef, on_delete=m.CASCADE))

# ## bma

Year = make_type('Year', m.IntegerField())

InOut_CHOICES = (('i', 'In'), ('o', 'Out'),)
InOut = make_type('InOut', 
    m.CharField(max_length=1, choices=InOut_CHOICES))

PubPriv_CHOICES = (('u', 'Public'),('r', 'Private'),)
PubPriv = make_type('PubPriv', m.CharField(max_length=1, choices=PubPriv_CHOICES))

Rdb_CHOICES = (('n', 'No'),('j', 'Ju'),('g', 'Ge'),)
Rdb = make_type('Rdb', m.CharField(max_length=1, choices=Rdb_CHOICES))

ProjectType = make_type('ProjectType', m.ForeignKey(TypeRef, on_delete=m.CASCADE))
MoGo = make_type('MoGo', m.ForeignKey(ContactRef, on_delete=m.CASCADE))
Program = make_type('Program', m.ForeignKey(ProgramRef, on_delete=m.CASCADE))
Description = make_type('Description', m.TextField())
Manager = make_type('Manager', m.ForeignKey(User, on_delete=m.CASCADE, related_name='+'))
Process = make_type('Process', m.ForeignKey(ProcessRef, on_delete=m.CASCADE))

# class FeeType(T):
#     A = 'a'
#     B = 'b'
#     C = 'c'
#     D = 'd'
#     CHOICES = (
#         (A, 'Fixe'),
#         (B, 'Mixte'),
#         (C, 'Fixe forfait'),
#         (D, 'Fourchette forfait'),
#     )
#     value = m.CharField(max_length=1, choices=CHOICES)

# # class FeeRate(T):
# #     value = ranges.NumericRange()

# class StudyFee(T):
#     value = m.FloatField()

# class Fee(T):
#     value = m.FloatField()
    
# class News(T):
#     value = m.BooleanField()

# class BmaAvis(T):
#     value = m.DateField()

# class BmaCand(T):
#     value = m.DateField()

# class BmaOffre(T):
#     value = m.DateField()

# class BmaComite(T):
#     value = m.DateField()

# class BmaCandidat(T):
#     value = m.IntegerField()

# class BmaSoumis(T):
#     value = m.IntegerField()

# class BmaDefr(T):
#     value = m.IntegerField()

# class Expert(T):
#     value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

# class Tenderer(T):
#     value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)

# class Winner(T):
#     value = m.ForeignKey(ContactRef, on_delete=m.CASCADE)


# ## logement 





# ## ecole


# ## draft

# class Nova(T):
#     value = m.IntegerField()

# # class ProjectType(T):
# #     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class BuildingType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class HousingType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class SpaceType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class InfraType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class PlanningType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)

# class InterventionType(T):
#     value = m.ForeignKey(TypeRef, on_delete=m.CASCADE)


