from __future__ import unicode_literals

from django.db import models

class Film(models.Model):
    FILM_RATINGS = (
        ('UNRATED', 'Not Rated'),
        ('PG', 'PG'),
        ('PG13', 'PG-13'),
        ('APPROVED', 'Approved'),
        ('PASSED', 'Passed'),
        ('G', "G"),
        ('R', 'R')
    )
    FILM_MEDIAS = (
        ('CD', 'CD'),
        ('DVD', 'DVD')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    alias = models.CharField(max_length=256, null=True)
    version = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    copies = models.IntegerField(default=1)
    media = models.CharField(max_length=4, choices = FILM_MEDIAS, default='DVD')
    rating = models.CharField(max_length=16, null=True, choices = FILM_RATINGS)

class FilmLanguage(models.Model):
    LANGUAGES = (
        ('ENGILISH', 'English'),
        ('SPAINISH', 'Spainish'),
        ('FRENCH', 'French')
    )
    CATEGORIES = (
        ('LANG', 'Languages'),
        ('Closed-Caption', 'Closed Captions')
    )
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='related film')
    language = models.CharField(max_length=16, choices = LANGUAGES)
    category = models.CharField(max_length =16, choices = CATEGORIES, default = CATEGORIES[0][0])
    
class FilmAward(models.Model):
    AWARDS = (
        ('OSCAR', 'Oscar'),
        ('NA', 'na')
    )
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='related film')
    award = models.CharField(max_length = 16, choices = AWARDS)
    
class FilmGenre(models.Model):
    GENRES = (
        ('FAMILAY', 'Family'),
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('ADVENTURE', 'Adventure'),
        ('ROMANCE', 'Romance'),
        ('CHRISTMAS', 'Christmas'),
        ('MYSTERY', 'Mystery'),
        ('THRILLER', 'Thriller'),
        ('CRIME', 'Crime'),
        ('WAR', 'War'),
        ('HISTORY', 'History'),
        ('FILM-NOIR', 'Film-noir'),
        ('SPORTS', 'Sports'),
        ('MUSICAL', 'Musical'),
        ('BIOGRAPHY', 'Biography'),
        ('SCIENCE', 'Science'),
        ('FICTION', 'Fiction'),
        ('HORROR', 'Horror'),
        ('SUSPENSE', 'Suspense'),
        ('DISASTER', 'Disaster'),
        ('INDEPENDENT', 'Independent'),
        ('BIOGRAPHICAL', 'Biographical'),
        ('INDIE', 'Indie'),
        ('WESTERN', 'Western'),
        ('DOCUMENTARY','Documentary'),
        ('ANIMATION', 'Animation'),
        ('FANTASY', 'Fantasy'),
        ('SUPERNATURAL', 'Supernatural'),
        ('EPIC', 'Epic'),
        ("CHILDRENS-LITERATURE", "Children's literature"),
        ("PERIOD", 'Period')
    )
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='related film')
    genre = models.CharField(max_length=16, choices=GENRES)
    
class FilmStaff(models.Model):
    ROLES = (
        ('DIRECTOR', 'Director'),
        ('CAST', 'Cast'),
    )
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='related film')
    role = models.CharField(max_length=16, choices=ROLES)
    name = models.CharField(max_length=128)
    
