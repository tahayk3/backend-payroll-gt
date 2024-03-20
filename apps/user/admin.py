from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información Personal', {'fields': ['email', 'username']}),
        ('Información Adicional', {'fields': ['role', 'picture', 'password', 'company', 'is_active', 'is_default_password']}),
    ]
    
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
    
admin.site.register(User, UserAdmin)
 