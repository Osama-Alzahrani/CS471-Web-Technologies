from django.shortcuts import render,redirect
from .models import Student,Address,Student2
from .forms import StudentForm,StudentFormMany
from .forms import UserRegisterForm
from django.db.models import Count
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url="user.loginView")
def view_students(request):
  allStudent=Student.objects.all()
  return render(request, 'usermodule/show_students.html', {'users':allStudent})

def view_cities(request):
    objs = Address.objects.annotate(num_students=Count('student'))

    # Render the template with annotated address data
    return render(request, 'usermodule/show_cities.html', {'addresses': objs})

def add_student(request):
  if request.method=='POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('user.view_students')
  else: 
    form = StudentForm(None)
  return render(request, "usermodule/add_student.html", {'form':form})

def update_student(request, SID):
  allStudent=Student.objects.get(id=SID)
  if request.method=='POST':
    form = StudentForm(request.POST , instance=allStudent)
    if form.is_valid():
      form.save()
      return redirect('user.view_students')
  form = StudentForm(instance=allStudent)
  return render(request, "usermodule/update_student.html", {'form':form})

def delete_student(request,SID):
  student = Student.objects.get(id=SID)
  student.delete()
  return redirect('user.view_students')

def multi_add_student(request):
  if request.method=='POST':
    form = StudentFormMany(request.POST)
    if form.is_valid():
      form.save()
      return redirect('user.multi_view_students')
  else: 
    form = StudentFormMany(None)
  return render(request, "usermodule/add_student.html", {'form':form})

def multi_update_student(request, SID):
  allStudent=Student2.objects.get(id=SID)
  if request.method=='POST':
    form = StudentFormMany(request.POST , instance=allStudent)
    if form.is_valid():
      form.save()
      return redirect('user.multi_view_students')
  form = StudentFormMany(instance=allStudent)
  return render(request, "usermodule/update_student.html", {'form':form})

def multi_delete_student(request,SID):
  student = Student2.objects.get(id=SID)
  student.delete()
  return redirect('user.multi_view_students')

def multi_view_students(request):
  allStudent=Student2.objects.all()
  return render(request, 'usermodule/show_Many_students.html', {'users':allStudent})

def register(request):
  if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f'Account created for {username}!')
          return redirect('user.login')  # Redirect to the login page
  else:
      form = UserRegisterForm()
  return render(request, "usermodule/usermanage/register.html", {"form": form})

def loginView(request):
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('user.view_students')  # Replace 'home' with the name of your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password')
  return render(request, "usermodule/usermanage/login.html")

def logoutUser(request):
  logout(request)
  return redirect('user.loginView')