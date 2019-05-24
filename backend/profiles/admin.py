from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.UserProfiles)
admin.site.register(models.ProfileFeedItem)