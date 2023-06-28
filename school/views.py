from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import TeacherChangeForm, TeacherCreationForm, StudentCreate
from .models import Student, School, Class


class HomePageView(generic.TemplateView):
    template_name = "school/home.html"


class SignUpView(generic.CreateView):
    form_class = TeacherCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"


class StudentListView(generic.ListView):
    model = Student
    template_name = "school/student_list.html"
    context_object_name = "students"


class StudentCreateView(generic.CreateView):
    form_class = StudentCreate
    template_name = "school/student_create.html"
    success_url = reverse_lazy("student_list")


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = "school/student_detail.html"
    context_object_name = "student"


class StudentEditView(generic.UpdateView):
    model = Student
    form_class = StudentCreate
    template_name = "school/student_edit.html"
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        return super().form_valid(form)


class ClassCreateView(generic.CreateView):
    model = Class
    fields = "__all__"
    template_name = "school/class_create.html"
    success_url = reverse_lazy("student_list")
