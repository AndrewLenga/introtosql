from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Book(models.Model):
    title = models.CharField(_("title"), max_length=255)
    author = models.CharField(_("author"), max_length=255)
    average_rating = models.FloatField(_("average_rating"))
    isbn = models.CharField(_("isbn"), max_length=150)
    isbn13 = models.CharField(_("isbn13"), max_length=150)
    language_code = models.CharField(_("language_code"),max_length=10)
    num_pages = models.IntegerField(_("num_pages"))
    ratings_count = models.BigIntegerField(_("ratings_count"))
    text_review_count = models.BigIntegerField(_("text_review_count"))
    publication_date = models.DateField(_("publication_date"))
    publisher = models.CharField(_("publiser"), max_length=150)

