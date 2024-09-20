from django.db import models
import random
import string

# Create your Functions to help models.

def generateUniqueCode():
    length = 6
    while True:
        code = ''.join(random.choice(string.ascii_uppercase ,k = length))
        if Room.objects.filter(code = code).count() == 0:
            break
    return code



# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length = 8,default='')
    host = models.CharField(max_length = 50, default = '', unique = True)
    votesToSkip = models.IntegerField(default = 1, null = False)
    guestCanPause = models.BooleanField(null = False, default = False)
    createdAt = models.DateTimeField(auto_now_add = True)
