from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

ALLOWED_EXTENSIONS =['flac','ogg','mp3','wav']


class Sermon(models.Model):
  title = models.CharField(max_length=500,verbose_name='Title')
  slug = models.SlugField(verbose_name='Slug',unique=True,editable=False)
  description = models.TextField(verbose_name='Description')
  author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Author')
  file = models.FileField(verbose_name='Sermon File',upload_to='sermon_uploads',validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
  thumbnail = models.ImageField(verbose_name='Sermon Thumbnail',upload_to='sermon_thumbnails')
  
  # def save(self):
  #   self.slug = slugify(self.title)
  #   super(Sermon,self).save()
  def save(self, *args, **kwargs):
      if not self.slug:
          slug_candidate = slugify(self.title)
          unique_slug = slug_candidate
          number = 1
          while Sermon.objects.filter(slug=unique_slug).exists():
              unique_slug = f"{slug_candidate}-{number}"
              number += 1
          self.slug = unique_slug
      super().save(*args, **kwargs)
    
  def __str__(self):
    return f'{self.title} by {self.author.username}'
  
class Review(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)
  sermon = models.ForeignKey(Sermon,on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date']
  
  def __str__(self):
    return self.text
