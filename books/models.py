from django.db import models

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
    authors = models.ManyToManyField(Author, related_name='books')
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    borrowing_duration = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title}  -  {self.authors}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class BookStatus(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('waiting', 'Waiting'),
        ('returned', 'returned')
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='statuses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book} borrowed by {self.user}"

    class Meta:
        verbose_name = "Book status"
        verbose_name_plural = "Book statuses"


class BookReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user}'s comment to {self.book}"

    class Meta:
        verbose_name = "Book Review"
        verbose_name_plural = "Book Reviews"

