from django.db import models
from django.contrib.auth.models import User



#  Event Model

class Event(models.Model):

    STATUS_CHOICES = (

        ('Upcoming', 'Upcoming'),

        ('Ongoing', 'Ongoing'),

        ('Completed', 'Completed'),
    )

    name = models.CharField(max_length=100)

    date = models.DateField()

    location = models.CharField(max_length=100)

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Upcoming'
    )

    def __str__(self):

        return self.name



#  Registration Model

class Registration(models.Model):

    student_name = models.CharField(
        max_length=100
    )

    student_email = models.EmailField()

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    def __str__(self):

        return f"{self.student_name} - {self.event.name}"


#  Feedback Model

class Feedback(models.Model):

    student_name = models.CharField(
        max_length=100
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    def __str__(self):

        return f"{self.student_name} - {self.event.name}"



#  User Profile Model

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=10,
        default='student'
    )

    def __str__(self):

        return self.user.username