from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    images = models.ImageField(upload_to = 'image/')
    title = models.CharField(max_length =30)
    description = models.TextField()
   
class Student(models.Model):
    first_name = models.CharField(max_length =60)
    last_name = models.CharField(max_length =60)
    education_level = models.CharField(max_length =120)
    student_email = models.EmailField()
    @classmethod  
    def search_by_first_name(cls,search_term):
        student = cls.objects.filter(first_name__icontains=search_term)
        return student
        
class Freelancer(models.Model):
    freelancer_names = models.CharField(max_length =60)
    project_name = models.CharField(max_length =60)
    freelancer_email = models.EmailField()


class Enterprise(models.Model):
    enterprise_founder = models.CharField(max_length =60)
    enterprise_name = models.CharField(max_length =60)
    enterprise_location = models.CharField(max_length =30)
    entrprise_email = models.EmailField()

    
class Business(models.Model):
    business_founder = models.CharField(max_length =60)
    business_name = models.CharField(max_length =60)
    business_location = models.CharField(max_length =30)
    business_email = models.EmailField()

    
class Academic(models.Model):
    academic_name = models.CharField(max_length =60)
    academic_location = models.CharField(max_length =60)
    academic_email = models.EmailField()

    
class Government(models.Model):
    institution_name = models.CharField(max_length =60)
    institution_location = models.CharField(max_length =60)
    institution_adress = models.IntegerField()

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class studentApplying(models.Model):
    first = models.CharField(max_length =20,null=True)
    last =  models.CharField(max_length =20 ,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    identity =  models.CharField(max_length =20 ,null=True)
    level = models.CharField(max_length =20 ,null=True)
    college = models.CharField(max_length =20 ,null=True)
    language= models.CharField(max_length =20 ,null=True)

    def _def_(self):
        return self.email


class businessEntApplying(models.Model):
    business_founder = models.CharField(max_length =20,null=True)
    business_name =  models.CharField(max_length =20 ,null=True)
    business_location = models.CharField(max_length =20, null=True)
    business_email = models.EmailField(null=True)
    contact_number =  models.IntegerField(null=True)
    business_type = models.CharField(max_length =20 ,null=True)
    message = models.TextField(max_length =20 ,null=True)
    other = models.TextField(max_length =20 ,null=True)

    def _def_(self):
        return self.business_email

   