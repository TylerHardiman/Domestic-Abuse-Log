

from django.db import models


# Create your models here.


class Survivor(models.Model):
    Survivor = models.ForeignKey('Survivor', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class AbuseLog(models.Model):
    post = models.ForeignKey(Survivor,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    timeAnd_Date = models.DateTimeField(auto_now_add=True, default = 'time and date created')
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)