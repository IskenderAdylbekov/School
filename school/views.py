from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings


from .forms import (
    TeacherChangeForm,
    TeacherCreationForm,
    StudentCreate,
    EmailMessageForm,
)
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
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")

        if search_query:
            queryset = queryset.filter(
                Q(full_name__icontains=search_query)
                | Q(email__icontains=search_query)
                | Q(student_class__name__icontains=search_query)
            )
        return queryset


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


class StudentDeleteView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy("student_list")
    template_name = "school/student_delete.html"


class ClassCreateView(generic.CreateView):
    model = Class
    fields = "__all__"
    template_name = "school/class_create.html"
    success_url = reverse_lazy("student_list")


def send_email(request):
    if request.method == "POST":
        form = EmailMessageForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data["recipients"].split(",")
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
            # You can also add additional logic here, like saving the sent message to a database.
            return redirect(
                "student_list"
            )  # Replace 'success' with the URL name for a success page
    else:
        form = EmailMessageForm()

    return render(request, "school/email_form.html", {"form": form})
