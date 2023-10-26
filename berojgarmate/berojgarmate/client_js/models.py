from django.db import models

# Create your models here.

class job_seeker_details(models.Model):
    first_name = models.CharField(null=True, blank=True,max_length=40)
    last_name = models.CharField(null=True, blank=True, max_length=40)
    # profile_image = models.ImageField(upload_to='profile_images/')
    city = models.CharField(null=True, blank=True,max_length=10)
    state = models.CharField(null=True, blank=True,max_length=40)
    Email_id = models.CharField(null=True, blank=True,max_length=40)
    gender=models.CharField(null=True, blank=True,max_length=40)
    date_of_birth = models.CharField(null=True, blank=True,max_length=40)
    # intrested_in = models.CharField(null=True, blank=True,max_length=40)
    education = models.CharField(null=True, blank=True,max_length=40)
    mobile_number = models.CharField(null=True, blank=True,max_length=40)

    def __str__(self):
        return self.first_name
