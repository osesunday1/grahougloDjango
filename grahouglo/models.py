from django.db import models




class ClientFeedback (models.Model):
    email= models.EmailField('Email Address', max_length=120)
    number= models.CharField('Client Number', max_length=20)
    name= models.CharField('Client Name', max_length=120)
    message= models.TextField('Client Message')
    
    def __str__(self):
        return self.name

    
