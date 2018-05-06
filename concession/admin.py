from django.contrib import admin
from .models import UserDetails, FormDetails, ChangeUserDetails

admin.site.register(UserDetails)
admin.site.register(FormDetails)
admin.site.register(ChangeUserDetails)