from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField( max_length=360)
    def no_of_ratings(self):
        ratings=Rating.objects.filter(movie=self)
        print(ratings)
        return len(ratings)
    def avg_ratings(self):
        avg_rating=Rating.objects.filter(movie=self).aggregate(Avg('stars'))
        avg_value=avg_rating['stars__avg']
        
        return round(avg_value,2) if avg_value is not None else 0


    
class Rating(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    Comment=models.CharField(max_length=360,null=True)

    class Meta:
        unique_together=(('user','movie'),)
        index_together=(('user','movie'),)
