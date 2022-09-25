from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField()
    resume = models.FileField(upload_to='resume',null=True)
    genderchoice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Decline to Answer','Decline to Answer'),
    ]
    statuschoices = [
        ('Pending','Pending'),
        ('Accepted','Accepted'),
        ('Not Accepted','Not Accepted')
    ]
    gender = models.CharField(choices = genderchoice, max_length = 21)
    status = models.CharField(choices = statuschoices, max_length = 15)
