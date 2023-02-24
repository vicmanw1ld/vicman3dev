from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='indexApp/images')
    
    created_day = models.DateTimeField(default=timezone.now)
    published_day = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        pass



    
