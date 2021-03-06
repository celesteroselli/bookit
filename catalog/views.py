import isbnlib
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import BookForm, EditBookForm, LoanAdd
from .models import Book, LoanInstance
from django.urls import reverse

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class BookSearchView(generic.ListView):
    model = Book

    def get_queryset(self):
        query = self.request.GET.get('q')
        filtered_list = Book.objects.filter(
            Q(title__contains=query) | Q(author__contains=query) | Q(isbn__contains=query)
        )
        return filtered_list
        
class LoanListView(generic.ListView):
    model = LoanInstance
    template_name = 'catalog/loan_list.html'  # Specify your own template name/location
    context_object_name = 'loan_list'

    def get_queryset(self):
        return LoanInstance.objects.all()

def book_detail(request, pk):
    instance = Book.objects.get(pk=pk)
    form = EditBookForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'catalog/book_detail.html', {'form': form})

def AddBook(request):
    form = BookForm(request.POST)
    if form.is_valid():
        Book = form.save(commit=False)
        Book.user = request.user
        Book.save()
        return redirect('books')
    return render(request, 'catalog/book_add.html', {'form': form})

def ReturnBook(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    loan = get_object_or_404(LoanInstance, book_loaned=instance)
    loan.delete()
    instance.status = 'AVAILABLE'
    instance.save()
    return redirect('books')

def AddLoan(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = LoanAdd(request.POST)
        if form.is_valid():
            LoanInstance = form.save(commit=False)
            LoanInstance.book_loaned = instance
            instance.status = 'ON LOAN'
            LoanInstance.user = request.user
            LoanInstance.save()
            instance.save()
            return redirect('books')

    form = LoanAdd()
    return render(request, 'catalog/loan_add.html', {'form': form})

def DeleteBook(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('books')

class FilterOverdue(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(status = 'ON LOAN')

def UserCreate(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'create_user.html', {'form': form})