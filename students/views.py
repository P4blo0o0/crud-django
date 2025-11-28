from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# Read - List all students
def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})

# Create - Add a new student
def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        Student.objects.create(name=name, age=age, course=course)
        return redirect('/')
    return render(request, 'students/create.html')

# Update - Edit a student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('/')
    return render(request, 'students/update.html', {'student': student})

# Delete - Remove a student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')
