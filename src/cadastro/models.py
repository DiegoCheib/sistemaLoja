from django.db import models

# Create your models here.
class userTest(models.Model):
    user_id = models.AutoField(primary_key=True, auto_created=True,)
    username = models.CharField(max_length=25)
    usersobrenome = models.CharField(max_length=25)
    useremail = models.CharField(max_length=100, unique=True)
    userpassword = models.CharField(max_length=50)
    telefone = models.CharField(max_length=17)
    cpf = models.CharField(max_length=11, unique=True)
    datacriacao = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.username}, {self.usersobrenome}"


#pra depois    
#data_nascimento = models.DateField()
