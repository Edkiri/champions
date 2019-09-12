"""User admin."""

# Django
from django.contrib import admin

# Models
from users.models import (
  User,
  Profile
)

class UserAdmin(admin.ModelAdmin):
  pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile, UserAdmin)