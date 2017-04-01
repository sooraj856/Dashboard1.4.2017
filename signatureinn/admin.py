from django.contrib import admin

# Register your models here.

from .models import Expense , Day , OtaRev

admin.site.register(Expense)
admin.site.register(Day)
admin.site.register(OtaRev)
