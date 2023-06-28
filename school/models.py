from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    student_class = models.ManyToManyField("Class", blank=True)
    address = models.TextField()
    sex = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="student_photos/", blank=True, null=True)

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.full_name


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    teacher_class = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        related_name="teachers",
        blank=True,
        null=True,
    )
    item_name = models.CharField(max_length=100)

    USERNAME_FIELD = "phone_number"  # Set the phone_number field as the username field for authentication
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self) -> str:
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    classes = models.ManyToManyField(Class)

    def __str__(self) -> str:
        return self.name
