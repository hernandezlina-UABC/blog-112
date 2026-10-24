from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# structured Query Language
# CREATE TABLE exenses (
#     id INTEGER PRIMARY_KEY AUTOINCREMENT,
#     name VARCHAR(100),
#)

# title, subtitle, body, author, date
class Post(models.Model):
    title = models.CharField(max_length=128) # Strings
    subtitle = models.CharField(max_length=128) # Strings
    body = models.TextField() # Large Sized String
    created_on = models.DateTimeField(auto_now_add=True) # Date and Time: MM / DD / YYYY HH:mm
    author = models.ForeignKey( # Creating a realtion to another label
        User,
        on_delete=models.CASCADE
    )
    
    def __str__(self): # To String -> "Hello World by admin"
        return f"{self.title} by {self.author}"
