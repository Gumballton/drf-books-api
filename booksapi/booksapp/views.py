import io

from django.http import FileResponse, HttpRequest
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from PIL import Image

from booksapp.serializers import BooksListSerializer
from booksapp.models import BooksModel

# Create your views here.

class BooksAPIListPagination(PageNumberPagination):

    """
    Pagination for the list of books.

    Attributes:
        page_size (int): Default page size.
        page_size_query_param (str): Query parameter to specify page size.
        max_page_size (int): Maximum page size.
    """

    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class BooksAPIListView(generics.ListAPIView):

    """
    View for the list of books API.

    Attributes:
        queryset (QuerySet): Query to fetch the list of books from the database.
        serializer_class (Serializer): Serializer for representing book data.
        pagination_class (Pagination): Pagination for the list of books.
    """

    queryset = BooksModel.objects.all().order_by('id')
    serializer_class = BooksListSerializer
    pagination_class = BooksAPIListPagination


class BookAPIDetailView(generics.RetrieveAPIView):

    """
    View for detailed information about a book API.

    Attributes:
        serializer_class (Serializer): Serializer for representing book data.
    """

    serializer_class = BooksListSerializer

    def get_queryset(self):
        """
        Retrieves the book's queryset by its identifier.

        Returns:
            QuerySet: Book queryset.
        """
        pk = self.kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'No such book ID'})
        
        queryset = BooksModel.objects.filter(pk=pk)
        return queryset
    

def get_image(request: HttpRequest, pk: int = None) -> FileResponse:
    """
    Returns the image of a book by its identifier.

    Args:
        request (HttpRequest): Client's request.
        pk (int): Book identifier.

    Returns:
        FileResponse: Response with the book's image.
    """
    if not pk:
        return Response({'error': 'No such book ID'})
    
    try:
        image_data = BooksModel.objects.get(pk=pk).book_image
    except BooksModel.DoesNotExist:
        return Response({'error': 'Указанный идентификатор книги не существует'})

    image = Image.open(io.BytesIO(image_data))
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="PNG")
    img_byte_array = img_byte_array.getvalue()

    return FileResponse(io.BytesIO(img_byte_array), content_type='image/png')
