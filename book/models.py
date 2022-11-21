from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()


class Book(models.Model):
    GENRE_CHOICE = (
        ("C", "Comedy"),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Science-Fiction"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(db_index=True, default="_")
    isbn = models.CharField(max_length=120)
    date_published = models.DateField()
    date_added = models.DateField(auto_now=True)
    edition = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICE, default="R")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author", related_name="books")

    class Author(models.Model):
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        email = models.EmailField(unique=True, )

    class Address(models.Model):
        number = models.PositiveIntegerField()
        street = models.CharField(max_length=255)
        city = models.CharField(max_length=255)
        zipcode = models.CharField(max_length=6, validators=[MinLengthValidator(5, "Code cannot be less than 5 digits"),
                                                             MaxLengthValidator(6, "Code cannot not exceed 6 digits")])
        Publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
