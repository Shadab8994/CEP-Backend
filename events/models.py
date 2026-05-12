# # # from django.db import models

# # # # Create your models here.
# # from django.db import models

# # class Event(models.Model):
# #     name = models.CharField(max_length=100)
# #     date = models.DateField()
# #     location = models.CharField(max_length=100)
# #     description = models.TextField()

# #     def __str__(self):
# #         return self.name
    

# # class Registration(models.Model):
# #     student_name = models.CharField(max_length=100)
# #     event = models.ForeignKey(Event, on_delete=models.CASCADE)

# #     def __str__(self):
# #         return self.student_name
    
# # class Feedback(models.Model):
# #     student_name = models.CharField(max_length=100)
# #     message = models.TextField()

# #     def __str__(self):
# #         return self.student_name
    
# # class Feedback(models.Model):
# #     student_name = models.CharField(max_length=100)
# #     message = models.TextField()

# #     def __str__(self):
# #         return self.student_name


# from django.db import models



# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     date = models.DateField()
#     location = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name



# class Registration(models.Model):
#     student_name = models.CharField(max_length=100)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.student_name} - {self.event.name}"



# class Feedback(models.Model):
#     student_name = models.CharField(max_length=100)
#     message = models.TextField()

#     def __str__(self):
#         return self.student_name
    

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('student', 'Student'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, default='student')  # student / admin

#     def __str__(self):
#         return self.user.username

from django.db import models
from django.contrib.auth.models import User


# 🔹 Event Model
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# 🔹 Registration Model
class Registration(models.Model):
    student_name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_name} - {self.event.name}"


# 🔹 Feedback Model
class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.student_name


from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='student')

    def __str__(self):
        return self.user.username