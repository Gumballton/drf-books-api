from django.db import models

# Create your models here.

class BooksModel(models.Model):
    author = models.CharField(max_length=1000)
    book_name = models.CharField(max_length=3000)
    book_link = models.CharField(max_length=3000)
    book_image = models.BinaryField(null=True)

    # If you have the table in db
    class Meta:
        # Provide the name of your existing table in the database
        db_table = 'books_data'

    def __str__(self):
        return self.book_name