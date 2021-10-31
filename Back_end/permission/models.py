from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class AuthUser(AbstractUser):
    student_id = models.IntegerField(db_column='student_id', unique=True, null=True, blank=True)

    class Meta:
        db_table = 'auth_user'
        managed = False
