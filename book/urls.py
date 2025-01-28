from django.urls import path

from book.views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
]