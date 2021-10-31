from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from permission.models import AuthUser

admin.site.register(AuthUser)
admin.site.register(Permission)
admin.site.register(ContentType)
