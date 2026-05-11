# # from django.db import models

# # # Create your models here.
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
#         return self.student_name
    
# class Feedback(models.Model):
#     student_name = models.CharField(max_length=100)
#     message = models.TextField()

#     def __str__(self):
#         return self.student_name
    
# class Feedback(models.Model):
#     student_name = models.CharField(max_length=100)
#     message = models.TextField()

#     def __str__(self):
#         return self.student_name


from django.db import models



class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Registration(models.Model):
    student_name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_name} - {self.event.name}"



class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.student_name
    
    