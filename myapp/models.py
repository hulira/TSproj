from django.db import models

# Create your models here.
class Staff_Details(models.Model):
    username = models.CharField(primary_key=True, null=False,blank=False,default=None,max_length=50)
    fname = models.CharField(null=False, blank=False, max_length=50)
    lname = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=50)

    def str(self):
        return self.username
    