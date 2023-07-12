from django.db import models
from django.contrib.auth.models import User # this will import the user(author here)
# Create your models here.


class Manual(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank = True)
    uploaded_by = models.CharField(max_length=200,null = True,blank = True)
    # author = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    def __str__(self):
        return self.title


# class material(models.Model):
#     name = models.CharField(max_length=100)
#     manual = models.ForeignKey(Manual, on_delete=models.CASCADE)
#     # pdf = models.FileField(upload_to='pdf')

#     def __str__(self):
#         return self.name
    


