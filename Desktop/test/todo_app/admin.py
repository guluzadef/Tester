from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import *
admin.site.register(Team)
admin.site.register(FB)