from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.db.models import Q

def index(request):
    search_query = request.GET.get('query', '')  # Handle search query
    if search_query:
        students = Student.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
    else:
        students = Student.objects.all()

    if request.method == "POST": 
        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(
                name=name,
                email=email
            )
            messages.success(request, "Student added successfully")
            return redirect('index')

        elif "update" in request.POST:
            id = request.POST.get("id")
            try:
                student = Student.objects.get(id=id)
                student.name = request.POST.get("name")
                student.email = request.POST.get("email")
                student.save()
                messages.success(request, "Student updated successfully")
            except Student.DoesNotExist:
                messages.error(request, "Student does not exist")
            return redirect('index')
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            try:
                Student.objects.get(id=id).delete()
                messages.success(request, "Student deleted successfully")
            except Student.DoesNotExist:
                messages.error(request, "Student does not exist")
            return redirect('index')

    context = {"students": students, "search_query": search_query}
    return render(request, 'index.html', context=context)
