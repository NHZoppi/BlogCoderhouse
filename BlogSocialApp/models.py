from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

    # Post de los usuarios
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.TextField(max_length= 255, null = False, blank = False)
    description = models.TextField(max_length=255, null = False, blank= False)
    content = RichTextField(blank= True, null = True)
    image = models.FileField(upload_to="media/", max_length=100)
    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.user.username}: {self.content}"
    
    def can_delete(self, user):
        return self.user == user

    def delete_post(self, user):
        if self.can_delete(user):
            self.delete()


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares',null=True, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'