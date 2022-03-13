from django import forms
from .models import Book, LoanInstance

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)

class BookAdd(forms.Form):
    title = forms.CharField(max_length=100)

class LoanAdd(forms.ModelForm):
    class Meta:
        model = LoanInstance
        exclude = ("user", "book_loaned",)

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)

