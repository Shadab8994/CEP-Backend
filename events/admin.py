from django.contrib import admin
from .models import Event

admin.site.register(Event)

from .models import Event, Registration

# admin.site.register(Event)
admin.site.register(Registration)