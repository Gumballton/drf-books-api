from rest_framework import serializers

from booksapp.models import BooksModel


class BooksListSerializer(serializers.ModelSerializer):

    """
    Serializer for listing books with their image URLs.
    """

    image_url = serializers.SerializerMethodField()

    class Meta:

        """
        Metadata about the serializer.

        Attributes:
            model (BooksModel): The model to be serialized.
            fields (tuple): The fields to include in the serialized output.
        """

        model = BooksModel
        fields = ('id', 'author', 'book_name', 'book_link', 'image_url')

    def get_image_url(self, obj: BooksModel) -> str:
        """
        Gets the URL of the book's image.

        Args:
            obj (BooksModel): The instance of the book model.

        Returns:
            str: The URL of the book's image.
        """
        return f'http://127.0.0.1:8000/api/v1/image/{obj.pk}/'