from django.contrib import admin

# Register your models here.

from .models import Prepations
from .models import Patiens
from .models import List_prepations

admin.site.register(Prepations)
admin.site.register(Patiens)
admin.site.register(List_prepations)