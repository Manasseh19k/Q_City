from django.db import models

# Create your models here.
class MeetOurTeam(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/album')
    position = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=13)

    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

