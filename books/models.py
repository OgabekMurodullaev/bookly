from django.db import models
from django.utils import timezone

from users.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category-images/', null=True, blank=True)

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='book-images/', null=True, blank=True)
    pages = models.IntegerField()
    borrowing_duration = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    objects = models.Manager

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class BookAuthors(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='authors')
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.book.__str__()} | {self.authors.__str__()}"


class Borrow(models.Model):
    STATUS_CHOICES = [
        ("borrowed", "Borrowed"),
        ("returned", "Returned"),
        ("overdue", "Overdue"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrows")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="borrowed")

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    def is_overdue(self):
        if self.status == "borrowed" and self.end_date < timezone.now().date():
            return True
        return False



class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    objects = models.Manager()


    def __str__(self):
        return f"{self.user}'s comment to {self.book}"

    class Meta:
        verbose_name = "Book Review"
        verbose_name_plural = "Book Reviews"


