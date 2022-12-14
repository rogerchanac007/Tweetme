from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError("No puede ser abc")
    return content

# Create your models here.
class Tweet(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)