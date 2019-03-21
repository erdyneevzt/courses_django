from django.db import models

# Create your models here.

class Author1(models.Model):

    CHOISES_FOR_CITY = (
        ('Moscow',"Москва"),
        ('Saint-Petersburgh', "Санкт-Петербург"),
        ('Novgorod',"Новогород"),
        ('Tomsk', "Томск"),
    )

    name = models.CharField(max_length=200,verbose_name="Имя автора")
    surname = models.CharField(max_length=200,verbose_name="Фамилия автора")
    city = models.CharField(choices=CHOISES_FOR_CITY, max_length=200,verbose_name="Город", help_text="Выберите город со списка")

    def __str__(self):
        return 'Имя %s' %self.name


class Article(models.Model):
    author = models.ForeignKey(Author1, verbose_name="Автор статьи", on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    text = models.TextField(max_length=500,verbose_name="Текст статьи")

    def __str__(self):
        return self.title