from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    class UserType(models.TextChoices):
        LIBRARIAN = 'librarian', 'Librarian'
        BOOKWORM = 'bookworm', 'Bookworm'
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    user_type = models.CharField(max_length=9, choices=UserType.choices, default=UserType.BOOKWORM)

    def __str__(self):
        return f"{self.username}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_image = models.ImageField(upload_to='profile-images/', null=True, blank=True)

    objects = models.Manager
    def __str__(self):
        return f"{self.user.id}"


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    objects = models.Manager()

    def __str__(self):
        return f"{self.follower} follows {self.followed}"

