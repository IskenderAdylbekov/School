from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Student(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField()
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    student_class = models.ManyToManyField("Class", blank=True, verbose_name="Класс")
    address = models.TextField(verbose_name="Адрес")
    sex = models.CharField(max_length=10, verbose_name="пол")
    photo = models.ImageField(
        upload_to="student_photos/", blank=True, null=True, verbose_name="Фото"
    )

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name_plural = "Ученики"
        verbose_name = "Ученик"


class Teacher(AbstractUser):
    phone_number = models.CharField(
        max_length=20, unique=True, verbose_name="Номер телефона"
    )
    teacher_class = models.ForeignKey(
        "Class",
        on_delete=models.CASCADE,
        related_name="teachers",
        blank=True,
        null=True,
        verbose_name="Класс",
    )
    item_name = models.CharField(max_length=100, verbose_name="Предмет")

    USERNAME_FIELD = "phone_number"  # Set the phone_number field as the username field for authentication
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "Учителя"
        verbose_name = "Учитель"

    def __str__(self):
        return self.get_full_name()


class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название класса")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Учитель"
    )
    students = models.ManyToManyField(Student, blank=True, verbose_name="Ученики")

    # def get_absolute_url(self):
    #     return reverse("class_list", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Классы"
        verbose_name = "Класс"

    def __str__(self) -> str:
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name="Школа")
    classes = models.ManyToManyField(Class, verbose_name="Классы")

    class Meta:
        verbose_name_plural = "Школа"

    def __str__(self) -> str:
        return self.name
