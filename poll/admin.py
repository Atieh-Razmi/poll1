from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Poll)
admin.site.register(Category)
admin.site.register(Vote)
admin.site.register(Choice)
