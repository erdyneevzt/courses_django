from django.db import models

# Create your models here.
class Example(models.Model):
    integer_field           = models.IntegerField()
    positive_field          = models.PositiveIntegerField()
    positive_small_field    = models.PositiveSmallIntegerField()
    big_integer_field       = models.BigIntegerField()
    float_field             = models.FloatField()
    binary_field            = models.BinaryField()
    boolean_field           = models.BooleanField()
    char_field              = models.CharField(max_length=5)
    text_field              = models.TextField(max_length=20)
    date_field              = models.DateField(auto_now=True)
    date_time_field         = models.DateTimeField(auto_now_add=True)
    decimal_field           = models.DecimalField(max_digits=8, decimal_places=2)
    email                   = models.EmailField()
    file_field              = models.FileField(upload_to= 'file')
    image_field             = models.ImageField(upload_to= 'images')

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_birth = models.DateField(auto_now=False)

    def __str__(self):
        return self.name + '' + self.surname

class Book(models.Model):
    CHOISE_GENRE = (
        ('comedy',"Comedy"),
        ('tragedy', "Tragedy"),
        ('drama', "Drama"),
    )
    author  = models.ForeignKey(Author, on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    text    = models.TextField(max_length=1000)
    genre   = models.CharField(max_length=50,choices=CHOISE_GENRE)

    def __str__(self):
        return self.title
