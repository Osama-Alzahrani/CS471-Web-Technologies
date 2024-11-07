from django.shortcuts import render
from .models import Student,Address
from django.db.models import Count, Min, Max, Sum, Avg

def view_students(request):
  allStudent=Student.objects.all()
  return render(request, 'usermodule/show_students.html', {'users':allStudent})

def view_cities(request):
    objs = Address.objects.annotate(num_students=Count('student'))

    # Render the template with annotated address data
    return render(request, 'usermodule/show_cities.html', {'addresses': objs})