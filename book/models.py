from django.db import models
from django.core.validators import RegexValidator


numeric_validator = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
date_validator = RegexValidator(r'^[0-9-]*$', 'Only date format YYYY-MM are allowed .') 


class Book(models.Model):

    LANGUAGE_TYP_CHOICES = (
        ('pl', 'pl'),
        ('en', 'en'),
        ('it', 'it'),
        ('de','de'),
        ('es','es'),
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=7, validators=[date_validator])
    isbn = models.CharField(max_length=13, blank = True)
    pages_number = models.PositiveIntegerField(blank = True)
    link_url = models.URLField(blank = True)
    pub_language = models.CharField(max_length=100, choices = LANGUAGE_TYP_CHOICES ) 
 

    def __str__(self):
        return f'{self.title} - {self.author}'