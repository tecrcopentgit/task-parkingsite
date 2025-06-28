from django.urls import path
from . import views
app_name = 'taskapp'
urlpatterns = [
    path('',views.homepage,name='home'),
    path('about',views.aboutpage,name='about'),
    path('parking',views.parkingpage,name='parking'),
    path('fastag',views.fastagpage,name='fastag'),
    path('service',views.servicepage,name='service'),
    path('career',views.careerpage,name='career'),
    path('contact',views.contactpage,name='contact'),
]