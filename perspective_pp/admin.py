from django.contrib.admin import site

# Register your models here.


from .models import *

site.register(Project)
site.register(Process)
site.register(ProcessItem)
site.register(StartTime)
site.register(EndTime)
site.register(Name)
site.register(Note)
site.register(Point)
site.register(Polygon)
site.register(Step)
