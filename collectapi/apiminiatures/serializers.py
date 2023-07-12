from rest_framework import serializers
from .models import Category, SubCategory, Miniature

class CategorySerializer(serializers.ModelSerializer):
  
  class Meta:
      model = Category
      fields = ['id', 'name']
class SubCategorySerializer(serializers.ModelSerializer):
  
  class Meta:
      model = SubCategory
      fields = ['id', 'category', 'name']

class MiniatureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Miniature
    exclude = ['modified', 'is_removed']