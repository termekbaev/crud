from django.urls import path

from book.views import BookView

urlpatterns = [
    path('', BookView.as_view({'get': 'list', 'post': 'create'}), name='book-list'),
    path('<pk>/', BookView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='book-detail'),
]