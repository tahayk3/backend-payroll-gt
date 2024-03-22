from django.contrib import admin
from .models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')
    list_filter = ('is_active',)
    search_fields = ('name',)

admin.site.register(Company, CompanyAdmin)

