from rest_framework import serializers
from .models import Category, SubCategory, Miniature

class SubCategorySerializer(serializers.ModelSerializer):
  category_name = serializers.CharField(read_only=True, source="category.name")
  class Meta:
    model = SubCategory
    fields = ['id', 'category','category_name', 'name']
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'created', 'name', 'subcategories']
  subcategories = SubCategorySerializer(many=True)
class MiniatureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Miniature
    exclude = ['modified', 'is_removed']