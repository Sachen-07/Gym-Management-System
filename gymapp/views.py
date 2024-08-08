from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime, timedelta

def calculate_expiration_date(membership_type):
    current_date = datetime.now()
    if membership_type == "monthly":
        expiration_date = current_date + timedelta(days=30)
    elif membership_type == "quarterly":
        expiration_date = current_date + timedelta(days=90)
    elif membership_type == "yearly":
        expiration_date = current_date + timedelta(days=365)
    else:
        expiration_date = current_date
    return expiration_date

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        membership = request.POST.get("membership")
        expiration_date = calculate_expiration_date(membership)
        
        Todo.objects.create(
            name=name,
            email=email,
            age=age,
            phone=phone,
            gender=gender,
            membership=membership,
            expiration_date=expiration_date
        )
        return redirect("/members")
    return render(request, "registration.html")

def edit(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    context = {"todo": todo_obj}
    if request.method == "POST":
        todo_obj.name = request.POST.get("name")
        todo_obj.email = request.POST.get("email")
        todo_obj.age = request.POST.get("age")
        todo_obj.phone = request.POST.get("phone")
        todo_obj.gender = request.POST.get("gender")
        todo_obj.membership = request.POST.get("membership")
        todo_obj.expiration_date = calculate_expiration_date(todo_obj.membership)
        todo_obj.save()
        return redirect("/members")
    return render(request, "edit.html", context)

def delete(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect("/members")

def members(request):
    page = "Members"
    todo_objs = Todo.objects.all()
    context = {
        "Todos": todo_objs,
        "page": page,
    }
    return render(request, "members.html", context)

def home(request):
    page = "Valar Dohaeris GYM"
    context = {
        "page": page,
    }
    return render(request, "home.html", context)

def about(request):
    page = "About us"
    context = {
        "page": page,
    }
    return render(request, "about-us.html", context)
