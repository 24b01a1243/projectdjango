from django.db import models

class Student(models.Model):

    SKILLS_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('Web', 'Web Development'),
    ]

    MODE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    department = models.CharField(max_length=10)
    year = models.CharField(max_length=5)
    roll_no = models.CharField(max_length=20)

    address = models.TextField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    skills = models.CharField(max_length=100)   # stored as comma-separated
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)

    resume = models.FileField(upload_to='resumes/')
    about = models.TextField()
    agree = models.BooleanField()
