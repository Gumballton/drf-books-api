from django.urls import path

from booksapp import views

urlpatterns = [
    path('api/v1/all-books/', views.BooksAPIListView.as_view()),
    path('api/v1/all-books/<int:pk>/', views.BookAPIDetailView.as_view()),
    path('api/v1/image/<int:pk>/', views.get_image),
]
