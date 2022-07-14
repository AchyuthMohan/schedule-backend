from django.db import models
from xml.parsers.expat import model

class Todo(models.Model):
    title=models.CharField(max_length=100)
    lastdate=models.DateTimeField()
    iscompleted=models.BooleanField(default=False)
    

    def __str__(self):
        return self.title