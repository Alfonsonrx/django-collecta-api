from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategorySerializer, SubCategorySerializer, MiniatureSerializer
from .models import Category, SubCategory, Miniature
from rest_framework import status
from django.http import Http404

# Create your views here.
class Miniature_APIView(APIView):
  def get(self, request, format=None, *args, **kwargs):
    limit = int(self.request.query_params.get('limit', 10))
    offset = int(self.request.query_params.get('offset', 0))
    miniature = Miniature.objects.all()[offset:offset+limit]
    serializer = MiniatureSerializer(miniature, many=True)
    
    return Response(serializer.data)
  
  def post(self, request, format=None, *args, **kwargs):
    serializer = MiniatureSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
class CategoryMiniature_APIView(APIView):
  def get(self, request, category, subcategory, format=None, *args, **kwargs):
    limit = int(self.request.query_params.get('limit', 10))
    offset = int(self.request.query_params.get('offset', 0))
    miniature = Miniature.objects.filter(category=category, subcategory=subcategory)[offset:offset+limit]
    serializer = MiniatureSerializer(miniature, many=True)
    
    return Response(serializer.data)
class Miniature_APIView_Detail(APIView):
  def get_object(self, pk):
    try:
      return Miniature.objects.get(pk=pk)
    except Miniature.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    miniature = self.get_object(pk)
    serializer = MiniatureSerializer(miniature)
    return Response(serializer.data)
  
  def put(self, request, pk, format=None):
    miniature = self.get_object(pk)
    serializer = MiniatureSerializer(miniature, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  def delete(self, request, pk, format=None):
    miniature = self.get_object(pk)
    miniature.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Category_APIView(APIView):
  def get(self, request, format=None, *args, **kwargs):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    
    return Response(serializer.data)
  
  def post(self, request, format=None, *args, **kwargs):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
class Category_APIView_Detail(APIView):
  def get_object(self, pk):
    try:
      return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    category = self.get_object(pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
  
  def put(self, request, pk, format=None):
    category = self.get_object(pk)
    serializer = CategorySerializer(category, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  def delete(self, request, pk, format=None):
    category = self.get_object(pk)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class SubCategory_APIView(APIView):
  def get(self, request, format=None, *args, **kwargs):
    subcategory = SubCategory.objects.all()
    serializer = SubCategorySerializer(subcategory, many=True)
    
    return Response(serializer.data)
  
  def post(self, request, format=None, *args, **kwargs):
    serializer = SubCategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
class SubCategory_APIView_Detail(APIView):
  def get_object(self, pk):
    try:
      return SubCategory.objects.get(pk=pk)
    except SubCategory.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):
    subcategory = self.get_object(pk)
    serializer = SubCategorySerializer(subcategory)
    return Response(serializer.data)
  
  def put(self, request, pk, format=None):
    subcategory = self.get_object(pk)
    serializer = SubCategorySerializer(subcategory, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  def delete(self, request, pk, format=None):
    subcategory = self.get_object(pk)
    subcategory.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
