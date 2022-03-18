
from django.db import models

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class Survivor(models.Model):
    Survivor = models.ForeignKey(Survivor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
class AbuseLog(models.Model):
    AbuseLog = models.ForeignKey(AbuseLog,on_delete=models.CASCADE,related_name='comments')
    post = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)