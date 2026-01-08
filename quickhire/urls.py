
from django.contrib import admin
from django.urls import path, include
from quickhire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('', include('auth_app.urls')),
    path('jobs/', include('Jobs.urls')),
]
