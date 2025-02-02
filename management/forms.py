from django import forms

from .models import *
from .models import Book, Genre, Language

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'language', 'total_copies', 'available_copies', 'pic']
        
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),
            'language': forms.Select(),
        }


# LANGUAGE_CHOICES = [
#     ('', '---------'),
#     ('EN', 'English'),
#     ('SW', 'Swahili'),
# ]
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'
#         genre = forms.CharField(max_length=100, label='Genre')
#         language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label='Language')


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrower
        exclude = ['issue_date', 'return_date']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class RatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude=['student','book']

