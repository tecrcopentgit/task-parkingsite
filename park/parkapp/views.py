from django.shortcuts import render
INSTALLED_APP = 'parkapp'

# Create your views here.
def homepage(request):
    return render(request,'parkapp/home.html')

def aboutpage(request):
    return render(request,'parkapp/about.html',name='about')