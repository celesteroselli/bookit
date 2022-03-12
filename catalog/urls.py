from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('search/', views.BookSearchView.as_view(), name='book_search'),
    path('loans/', views.LoanListView.as_view(), name='loans'),
    path('book_add/', views.AddBook, name='book_add'),
    path('loan_add/<int:pk>/', views.AddLoan, name='loan_add'),
    path('book_delete/<int:pk>/', views.DeleteBook, name='book_delete'),
    path('filter/overdue/', views.FilterOverdue.as_view(), name='filter_overdue'),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("create_user/", views.UserCreate.as_view(), name="create_user"),
]