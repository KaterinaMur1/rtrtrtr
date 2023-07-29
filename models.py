from django.db import models

# Create your models here.

class Advertisements(models.Model):
    title = models.CharField('заголовок', max_length=100)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Возможен торг или нет')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    # @admin.display(description='дата создания')
    # def created_date(self):
    #     from django.utils import timezone
    #     if self.created_at.date() == timezone.now.date():
    #         created_time = self.created_at.time().strftime("%H:%M:%S")
    #         return format_html(
    #             '<span style="color: green; font-weight: bold;>Сегодня'
    #         )
    #     return self.

#Задание 4.1
class Meta:
    db_table = 'advertisements'

#Задание 4.2
def _str_(self) -> str:
    return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

