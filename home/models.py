from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    subject = models.TextField()
    date = models.DateField()
    

    def __str__(self):
        return self.name,self.email,self.phone,self.subject,self.date
    



