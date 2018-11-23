from django.contrib.admin import site

# Register your models here.

from .models.project import *
from .models.types import TYPES

site.register(Project)

for _, T in TYPES:
    site.register(T)
