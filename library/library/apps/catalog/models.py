from django.db import models  

class Author(models.Model):  
  full_name = models.TextField(verbose_name="Автор")  
  birth_year = models.SmallIntegerField(verbose_name="год рождения")  
  country = models.CharField(max_length=2, verbose_name="Страна")

  def __str__(self):
    return(self.full_name)
  
  class Meta:
    verbose_name = 'Автор'
    verbose_name_plural = 'Авторы'

class PublishingHouse(models.Model):
  name = models.TextField(verbose_name="Издательство")
  
  def __str__(self):
    return(self.name)
  
  class Meta:
    verbose_name = 'Издательство'
    verbose_name_plural = 'Издательства'

class Book(models.Model):  
  ISBN = models.CharField(max_length=13, verbose_name="ISBN")  
  title = models.TextField(verbose_name="Название")  
  description = models.TextField(verbose_name="Описание")  
  year_release = models.SmallIntegerField(verbose_name="Год издания")  
  author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
  copy_count = models.SmallIntegerField(default=1, verbose_name="Копий")
  price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
  ph_name = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, null=True, blank=True, related_name='books', verbose_name="Издательство")

  def __str__(self):
    return(self.title)
  
  class Meta:
    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'

