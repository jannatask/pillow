from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,verbose_name='Заполните ФИО' )

    email = models.EmailField(unique=True, verbose_name='Введите почту')

    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name