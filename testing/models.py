from django.db import models

# Create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length=312)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=26)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["author"]
        indexes = [
            models.Index(fields=["isbn"])
        ]
