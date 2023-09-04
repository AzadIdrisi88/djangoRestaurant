from django.db import models

# Create your models here.
class restroModel(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


    def __str__(self):
     return "username={0},name={1},password={2}".format(self.username,self.name,self.password)
    
class bookmodel(models.Model):
   category=models.CharField(max_length=100)
   author=models.CharField(max_length=100)
   name=models.CharField(max_length=100)

   def __str__(self):
      return "category={0},author={1},name={2}".format(self.category,self.author,self.name)