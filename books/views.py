# Create your views here.
from django import forms
from library.books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('count', 'create_at', 'update_at')
        widgets = {
            'isbn' : forms.RegexField(regex=r'^\d{13}$')
        }
