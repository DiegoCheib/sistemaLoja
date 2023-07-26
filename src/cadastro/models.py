from django.db import models

# Create your models here.
class userTest(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    usersobrenome = models.CharField(max_length=25, default="Sobrenome")

    def __str__(self):
        return f"{self.username}, {self.usersobrenome}"
