from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("user must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(
            email=email, name=name, password=password, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email


class College(models.Model):
    college_id = models.CharField(max_length=255, primary_key=True)
    num_emp = models.IntegerField()
    dean = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    num_teachers = models.IntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    dept_id = models.CharField(max_length=255, primary_key=True)
    head_of_department = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    college = models.ForeignKey("College", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ssn = models.CharField(max_length=255, primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    phone = models.CharField(max_length=255)
    birth = models.DateField()
    address = models.CharField(max_length=255)
    dept = models.ForeignKey("Department", on_delete=models.CASCADE)


# class Teacher(models.Model):
#     ssn = models.CharField(max_length=255, primary_key=True)
#     f_name = models.CharField(max_length=255)
#     l_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#     dob = models.DateField()
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255, null=True)


# class Exam(models.Model):
#     id_exam = models.CharField(max_length=255, primary_key=True)
#     score = models.FloatField()
#     num_of_std = models.IntegerField()
#     date = models.DateField()
#     name = models.CharField(max_length=255)
#     college = models.ForeignKey("College", on_delete=models.CASCADE)


# class Course(models.Model):
#     course_id = models.CharField(max_length=255, primary_key=True)
#     instructor_name = models.CharField(max_length=255)
#     course_name = models.CharField(max_length=255)
#     num_of_std = models.IntegerField()
#     teacher = models.ForeignKey(
#         "Teacher", on_delete=models.CASCADE, related_name="courses"
#     )
#     exam = models.ForeignKey("Exam", on_delete=models.CASCADE, related_name="courses")


# class College(models.Model):
#     college_id = models.CharField(max_length=255, primary_key=True)
#     num_emp = models.IntegerField()
#     dean = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     num_teachers = models.IntegerField()

#     def __str__(self):
#         return self.name


# class Employee(models.Model):
#     ssn = models.CharField(max_length=255, primary_key=True)
#     f_name = models.CharField(max_length=255)
#     l_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#     dob = models.DateField()
#     department = models.ForeignKey("Department", on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     college = models.ForeignKey("College", on_delete=models.CASCADE)


# class CourseGroup(models.Model):
#     coursegroup_id = models.CharField(max_length=255, primary_key=True)
#     course = models.ForeignKey("Course", on_delete=models.CASCADE)
#     group_link = models.CharField(max_length=255)
#     teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)


# class Company(models.Model):
#     company_id = models.CharField(max_length=255, primary_key=True)
#     website = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     college = models.ForeignKey("College", on_delete=models.CASCADE)
#     courses = models.CharField(max_length=255)


# class GraduationProject(models.Model):
#     project_id = models.CharField(max_length=255, primary_key=True)
#     title = models.CharField(max_length=255)
#     pdf_links = models.TextField()
#     teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)


# class Enrollment(models.Model):
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)
#     dept = models.ForeignKey("Department", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("student", "dept")


# class CompanyCourses(models.Model):
#     courses = models.CharField(max_length=255)


# class Register(models.Model):
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)
#     course = models.ForeignKey("Course", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("student", "course")


# class Teach(models.Model):
#     teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
#     course = models.ForeignKey("Course", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("teacher", "course")


# class DoExam(models.Model):
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)
#     exam = models.ForeignKey("Exam", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("student", "exam")


# class MakeExam(models.Model):
#     teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
#     exam = models.ForeignKey("Exam", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("teacher", "exam")


# class Partner(models.Model):
#     college = models.ForeignKey("College", on_delete=models.CASCADE)
#     company = models.ForeignKey("Company", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("college", "company")


# class GraduationProjectStudent(models.Model):
#     student = models.ForeignKey("Student", on_delete=models.CASCADE)
#     project = models.ForeignKey("GraduationProject", on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("student", "project")
