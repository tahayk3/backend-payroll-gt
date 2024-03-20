from django.contrib import admin
from django.urls import path, include
from user.urls import urlpatterns as users_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(users_urls)),

]