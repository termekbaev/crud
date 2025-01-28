from rest_framework.viewsets import ModelViewSet

from book.models import Book
from book.serializers import BookSerializer


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'