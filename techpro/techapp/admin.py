from django.contrib import admin
from techapp.models import Employee


@admin.register(Employee)
class Employeedmin(admin.ModelAdmin):
    list_display = ('id','person','groupp','age')

