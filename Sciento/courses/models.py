
from django.db import models
from users.models import Tutor, Student


PUBLIC = 'public'
INDIVIDUAL = 'individual'
COURSE_TYPE_CHOICES = [
        (PUBLIC, 'public'),
        (INDIVIDUAL, 'individual'),
    ]

class Course (models.Model):
    cours_id = models.AutoField(primary_key=True)
    type = models.CharField(
        max_length=10, 
        choices=COURSE_TYPE_CHOICES, 
        default=PUBLIC
    )
    def amountOfSubscribers():
        pass
    language = models.CharField(max_length=15)
    aSubscribers = amountOfSubscribers()    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0) 
    author = models.ManyToManyField(Student)
    def update_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            total_rating = sum(rating.value for rating in ratings)
            self.average_rating = total_rating / ratings.count()
        else:
            self.average_rating = 0
        self.save()

    def __str__(self):
        return f"Рейтинг: {self.value} для {self.course}"

    def enroll_student(self, student):
    
        if self.is_active and self.start_date > student.registration_date:
            self.students.add(student)
            return f"Student {student} has been successfully enrolled in the course {self.name}."
        else:
            return "Cannot enroll the student. The course is either inactive or already started."

    def unenroll_student(self, student):
   
        if student in self.students.all():
            self.students.remove(student)
            return f"Student {student} has been successfully removed from the course {self.name}."
        else:
            return "The student is not enrolled in this course."