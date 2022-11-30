from django import forms
from . import models

class AddBookForm(forms.ModelForm) :
    class Meta:
        model = models.Book
        fields = [
            'title',
            'isbn', 
            'author',
        ]
        labels = {
            'title' : 'Title',
            'isbn' : 'ISBN',
            'author' : 'Author',
        }

class IssueBookForm(forms.Form):

    class Meta:
        model = models.IssuedBooks
    isbn_ = forms.ModelChoiceField(queryset=models.Book.objects.all(),widget=forms.Select(attrs={'class':'form-control'}) , empty_label='Title|ISBN', to_field_name='isbn', label='Book Title' )
    user_ = forms.ModelChoiceField(queryset=models.User.objects.filter(is_superuser=False, is_staff=False, is_active=True),widget=forms.Select(attrs={'class':'form-control'}) , empty_label='Name|Email', to_field_name='email', label='Student') 


    