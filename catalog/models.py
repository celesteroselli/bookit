from django.db import models
import isbnlib
from django.contrib.auth.models import User
from django.urls import reverse
from isbnlib import *
from datetime import *

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    isbn = models.CharField('ISBN', max_length=10, unique=True,
                            help_text='10 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    title = models.CharField(max_length=30, null=True)

    author = models.CharField(max_length=10, null=True)

    LOAN_STATUS = (
        ('AVAILABLE', 'Available'),
        ('ON LOAN', 'On Loan'),
        ('ON HOLD', 'On Hold'),
    )

    GENRES = {
        ('REALISTIC FICTION', 'Realistic Fiction'),
        ('HISTORICAL FICTION', 'Historical Fiction'),
        ('SCIENCE FICTION', 'Science Fiction'),
        ('ADVENTURE', 'Adventure'),
        ('FANTASY', 'Fantasy'),
        ('HORROR', 'Horror'),
        ('MYSTERY', 'Mystery'),
        ('NON-FICTION', 'Non-fiction'),
    }

    genre = models.CharField(
        max_length=30,
        choices=GENRES,
        blank=True,
        help_text='Book Genre',
    )

    status = models.CharField(
        max_length=30,
        choices=LOAN_STATUS,
        blank=True,
        default='Available',
        help_text='Book Availabiliy',
    )

    def __str__(self):
        #String representing model object
        return self.title

class LoanInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    loaner = models.CharField(max_length=50, null=True)

    loaner_email = models.EmailField(blank=True, null=True)

    book_loaned = models.ForeignKey(Book, on_delete=models.CASCADE, 
                                    blank=False, null=True)
    
    due_date = date.today()+timedelta(days=21)

    if (date.today()<due_date):
        overdue = False

    loan_status = not overdue