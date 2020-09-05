from django.db import models

#code to remove html tags from body to create snippet
import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

CATEGORY_CHOICES = (
    ('health','HEALTH'),
    ('music','MUSIC'),
    ('study','STUDY'),
    ('programming','PROGRAMMING'),
    ('gaming','GAMING'),
    ('food','FOOD'),
    ('movies','MOVIES'),
    ('cartoons','CARTOONS'),
    ('mining','MINING')
)

class Category(models.Model):
    categ = models.CharField(max_length=250)

    def __str__(self):
        return self.categ

class Article(models.Model):
    topic= models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='gaming')

    def __str__(self):
        return self.topic

    def snippet(self):
        temp =  striphtml(self.body)
        return temp[:60] + '...'