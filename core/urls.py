from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.payrolls.urls', 'payrolls'), namespace='payrolls')),
    path('api/v1/', include('apps.employee.urls')),
    path("", include(("apps.services.urls", "services"))),
    path('api/v1/', include('apps.company.urls')),
    path('api/v1/', include('apps.user.urls')),
]

