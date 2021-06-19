from django.contrib import admin
from .models import Contact,MapUserContact,Profile

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(MapUserContact)

