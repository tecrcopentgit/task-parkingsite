from django.urls import path
from . import views
InstalledApps='parkapp'


urlpatterns=[
    path('',views.homepage,name='home'),
    path('/about',views.aboutpage,name='about'),
]