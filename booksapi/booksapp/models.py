from django.db import models

# Create your models here.

class BooksModel(models.Model):

    """
    Model for storing information about books.

    Attributes:
        author (str): The author's name of the book.
        book_name (str): The title of the book.
        book_link (str): The link to the book.
        book_image (bytes): The binary image data of the book.
    """

    author = models.CharField(max_length=1000)
    book_name = models.CharField(max_length=3000)
    book_link = models.CharField(max_length=3000)
    book_image = models.BinaryField(null=True)

    # If you have the table in db
    class Meta:
        # Provide the name of your existing table in the database
        db_table = 'books_data'

    def __str__(self) -> str:
        """
        Returns the string representation of the model object.

        Returns:
            str: The string representation of the model object.
        """
        return self.book_name