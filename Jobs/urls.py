from django.urls import path
from . import views


urlpatterns = [
    path('postjob/', views.postjob, name='postjob'),
]

