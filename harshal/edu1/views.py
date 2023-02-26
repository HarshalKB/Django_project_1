from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    
    courses = Course.objects.all()

    return render(request, 'index.html', {'courses' : courses})