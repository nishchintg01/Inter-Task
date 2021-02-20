from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Movies(models.Model):
    title = models.CharField(max_length=1000)
    Image = models.ImageField(upload_to = 'movies', default = 'default.png')
    Description = models.TextField()

    @property
    def Avg_rating(self):
        rating = 0
        for ratings in Comments.objects.filter(movie = Movies.objects.get(id=self.id)):
            rating += ratings.Rating
        try:
            return rating/Comments.objects.filter(movie = Movies.objects.get(id=self.id)).count()
        except:
            return 0
    

class Comments(models.Model):
    review =  models.TextField()
    Rating = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movies, related_name="comments" ,on_delete=models.CASCADE)
    Author = models.ForeignKey(User, related_name="author",on_delete=models.CASCADE)

    @property
    def ratings(self):
        return ["hi"]*int(self.Rating)
