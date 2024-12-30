from django.db import models
from django.utils import timezone
from users.models import Student, Tutor

class Session(models.Model):
    status_list = [
        (1, "planned"),
        (2, "active"),
        (3, "saved"),
        (4, "archived"),
        (5, "canceled")
    ]
    sessions_id = models.AutoField(primary_key=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.IntegerField(choices=status_list)
    platform_name = models.CharField(max_length=255)
    video_recording = models.FileField(upload_to='recordings/')
    link = models.URLField()
    student_identifier = models.IntegerField()
    tutor_identifier = models.IntegerField()

    def create_session(student_id: Student, tutor_id: Tutor, selected_time, duration, platform):
    
        time_end = selected_time + timezone.timedelta(minutes=duration)
    
        new_session = Session.objects.create(
            time_start=selected_time,
            time_end=time_end,
            status=1, 
            platform_name=platform,
            student_identifier=student_id,
            tutor_identifier=tutor_id
        )
    
        return new_session


    def start_recording(self):
        pass

    def stop_recording(self):
        pass

    def activate_link(self):
        pass

    def save_recording(self):
        pass

    def invite_student(self):
        pass

    def invite_tutor(self):
        pass

    def create_new_shared_board(self):
        pass
