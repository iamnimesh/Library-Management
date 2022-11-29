from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.PositiveBigIntegerField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title) + '|' + str(self.isbn)

class Student(models.Model):
    branches = [
        ('it', 'Information Technology'),
        ('cs', 'Computer Science'),
        ('csai', 'Computer Science & Artificial Intelligence'),
        ('csb', 'Computer Science & Business'),
        ('none', 'NONE')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=20)
    branch = models.CharField(max_length=60, choices = branches, default = 'none')
    # fine 
    # issued_books = models.ManyToManyField(Book, on_delete = models.CASCADE)
    def __str__(self):
        return self.user.first_name + '|' + str(self.enrollment_no)

    @property
    def get_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    @property
    def get_user_id(self):
        return self.user.id 

class IssuedBooks(models.Model):
    user = models.CharField(max_length=100)
    isbn = models.PositiveBigIntegerField()
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField(default = datetime.today() + timedelta(days = 15))

