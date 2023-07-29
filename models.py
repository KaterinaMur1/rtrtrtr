from django.db import models

# Create your models here.

class Advertisements(models.Model):
    title = models.CharField('заголовок', max_length=100)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Возможен торг или нет')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


#Задание 4.1
class Meta:
    db_table = 'advertisements'

#Задание 4.2
def _str_(self) -> str:
    return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

