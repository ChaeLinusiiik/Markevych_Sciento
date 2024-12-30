# Generated by Django 5.1.4 on 2024-12-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sessions_id', models.AutoField(primary_key=True, serialize=False)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(1, 'planned'), (2, 'active'), (3, 'saved'), (4, 'archived'), (5, 'canceled')])),
                ('platform_name', models.CharField(max_length=255)),
                ('video_recording', models.FileField(upload_to='recordings/')),
                ('link', models.URLField()),
                ('student_identifier', models.IntegerField()),
                ('tutor_identifier', models.IntegerField()),
            ],
        ),
    ]
