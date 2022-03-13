from django import forms
from .models import Book, LoanInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)

class LoanAdd(forms.ModelForm):
    class Meta:
        model = LoanInstance
        exclude = ("user", "book_loaned",)

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)

