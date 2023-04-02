from django.contrib import admin
from django.urls import path, include
from users.views import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('users/', include('users.urls', namespace='users')),
]
