from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models

ST = 'Student'
TR = 'Tutor'
AD = 'Admin'
ROLE_CHOICES = [
        (ST, 'student'),
        (TR, 'tutor'),
        (AD, 'admin')
]

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default= 'student')
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    about_me = models.TextField(max_length=500)
    level_of_knowledge = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    account_number = models.CharField(max_length=50)

    def login(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def enroll_to_tutor(self):
        pass

    def point_out_platform_issue(self):
        pass

    def send_message(self):
        pass

    def pay_for_lessons(self):
        pass

    def confirm_lessons(self):
        pass

    def enroll_to_course(self):
        pass

    def rate_course(self):
        pass

    def mark_homework(self):
        pass


class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tutor')
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    about_me = models.TextField(max_length=500)
    specialization = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    account_number = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)

    def login(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def confirm_enrollment(self):
        pass

    def confirm_payment(self):
        pass

    def report_user(self):
        pass

    def edit_profile(self):
        pass

    def send_message(self):
        pass

    def create_material(self):
        pass

    def evaluate_homework(self):
        pass

    def enroll_student_to_course(self):
        pass


class Admin(models.Model):
    admin_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    problem_types = models.JSONField()  
    chat_id = models.IntegerField()

    def login(self):
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def join_chat(self):
        pass

    def block_user(self):
        pass

    def cancel_verification(self):
        pass

    def assign_platform(self):
        pass

    def assign_link(self):
        pass

    def assign_rating(self):
        pass
