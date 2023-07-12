from django.db import models

from model_utils.models import SoftDeletableModel, TimeStampedModel

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.

class Category(TimeStampedModel, SoftDeletableModel):
  name = models.CharField(max_length=128)
  def __str__(self) -> str:
      return self.name
class SubCategory(TimeStampedModel, SoftDeletableModel):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=128)
  def __str__(self) -> str:
      return self.name

class Miniature(TimeStampedModel, SoftDeletableModel):
  category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
  name = models.CharField(max_length=32)
  width = models.DecimalField(decimal_places=1, max_digits=5)
  height = models.DecimalField(decimal_places=1, max_digits=5)

  diet = models.CharField(max_length=32, null=True, blank=True)
  period = models.CharField(max_length=32, null=True, blank=True)
  meaning = models.CharField(max_length=64, null=True, blank=True)

  fun_fact = models.TextField(max_length=256, null=True, blank=True)
  likes = models.PositiveIntegerField(default=0)
  def __str__(self) -> str:
      return str(self.id)+"-"+self.name