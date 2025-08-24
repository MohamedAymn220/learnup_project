from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Course
from .forms import CustomUserCreationForm, CourseForm

# ==================== الصفحة الرئيسية ====================
@login_required
def index(request):
    return render(request, "index.html", {"user": request.user})

# ==================== تسجيل المستخدم ====================
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


# ==================== تسجيل الدخول ====================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# ==================== عرض جميع الكورسات ====================
@login_required
def all_courses(request):
    courses = Course.objects.all().order_by("-created_at")
    return render(request, "all_courses.html", {"courses": courses})


# ==================== [الطالب يتفرج بس]  إضافة كورس (للمدرسين فقط) ====================
@login_required
def add_course(request):
    if request.user.role != "instructor":
        return redirect("all_courses")

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect("all_courses")
    else:
        form = CourseForm()
    return render(request, "add_course.html", {"form": form})


# ==================== تعديل الكورس ====================
@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user != course.created_by:
        
        return redirect("all_courses")

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()

            return redirect("all_courses")
    else:
        form = CourseForm(instance=course)

    return render(request, "edit_course.html", {"form": form, "course": course})


# ==================== حذف الكورس ====================
@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user != course.created_by:
        return redirect("all_courses")

    
    if request.method == "POST":
        course.delete()
        return redirect("all_courses")

    
    return redirect("all_courses")


# ==================== تسجيل الخروج ====================
def logout_view(request):
    logout(request)
    return redirect("login")

def view_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "view_course.html", {"course": course})

