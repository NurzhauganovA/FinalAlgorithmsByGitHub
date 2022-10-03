from django.contrib import admin
from .models import CustomUser, ProfileSettings


admin.site.register(CustomUser)
admin.site.register(ProfileSettings)