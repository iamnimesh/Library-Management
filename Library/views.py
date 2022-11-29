from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib.auth.models import User, Group
from . import models
from django.contrib import messages
from datetime import datetime, date, timedelta
# Create your views here.

# class RegisteredStudentsForm(forms.ModelForm) :
#     model = models.Student
#     fields = []

def login_view(request):
    return render(request, "Library/login.html")



def add_book_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = forms.AddBookForm(request.POST)
            if form.is_valid():
                form.save()
        form = forms.AddBookForm()
        details = models.Book.objects.all()
        return render(request, 'Library/addbook.html', {'form' : form, 'details' : details})
    else :
        return render(request, 'Library/index.html')
        
def displaybooks(request) :
    if request.user.is_superuser:
        books = models.Book.objects.all()
        return render(request, 'Library/displaybooks.html', {'books': books})
    else :
        return render(request, 'Library/index.html')

def issuebook(request):
    if request.user.is_superuser:
        form = forms.IssueBookForm()
        if request.method == 'POST' :
            form = forms.IssueBookForm(request.POST)
            if form.is_valid():
                o = models.IssuedBooks()
                o.user = request.POST['user_']
                o.isbn = request.POST['isbn_']
                o.save()
                return render(request, 'Library/bookIssuedSuccessful.html')
        return render(request, 'Library/issueBook.html', {'form' : form})
    else :
        return render(request, 'Library/index.html')

def viewissuedbooks(request) :
    if request.user.is_superuser:
        issued_books = models.IssuedBooks.objects.all()
        li = []
        for ib in issued_books:
            issue_date = str(ib.issue_date.day) + '-' + str(ib.issue_date.month) + '-' + str(ib.issue_date.year)
            return_date = str(ib.return_date.day) + '-' + str(ib.return_date.month) + '-' + str(ib.return_date.year)

            days = (date.today() - ib.issue_date)
            print(date.today())
            d = days.days
            fine = 0
            if d > 15:
                day = d-15
                fine = day*10
            books = list(models.Book.objects.filter(isbn = ib.isbn))
            students = list(models.User.objects.filter(email = ib.user))
            i = 0
            for l in books :
                t = (students[i].get_full_name, students[i].email, books[i].title, books[i].author, issue_date, return_date, fine)
                i += 1
                li.append(t)
        return render(request, 'Library/viewIssuedBooks.html', {'li' : li})
    else :
        return render(request, 'Library/index.html')

def viewstudents(request) :
    if request.user.is_superuser: 
        students = models.User.objects.filter(is_superuser=False, is_active=True, is_staff=False)
        return render(request, 'Library/viewStudents.html', {'students' : students})
    else :
        return render(request, 'Library/index.html')

def viewissuedbooksbystudent(request):
    if not request.user.is_superuser:
        student = models.User.objects.filter(id=request.user.id)
        issued_books = models.IssuedBooks.objects.filter(user=student[0].email)

        li1 = []
        li2 = []
        li3 = []
        t3 = (student[0].get_full_name, student[0].email)
        li3.append(t3)
        for ib in issued_books:
            books = models.Book.objects.filter(isbn = ib.isbn)
            for book in books:
                t = (book.title, book.author)
                li1.append(t)
            issue_date = str(ib.issue_date.day) + '-' + str(ib.issue_date.month) + '-' + str(ib.issue_date.year)
            return_date = str(ib.return_date.day) + '-' + str(ib.return_date.month) + '-' + str(ib.return_date.year)

            days = (date.today() - ib.issue_date)
            print(date.today())
            d=days.days
            fine=0
            if d>15:
                day=d-15
                fine=day*10
            t=(issue_date,return_date,fine)
            li2.append(t)
        return render(request, 'Library/issuedBookByStudent.html', {'li1' : li1, 'li2' : li2, 'li3' : li3})
    else:
        return render(request, 'Library/index.html')