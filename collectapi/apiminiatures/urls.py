from django.urls import path
from . import views

app_name = 'apiminiatures'
urlpatterns = [
  path('v1/miniatures', views.Miniature_APIView.as_view(), name='Miniatures'), 
  path('v1/miniatures/category/<int:category>/<int:subcategory>/', views.CategoryMiniature_APIView.as_view(), name='CatMiniatures'),
  path('v1/miniatures/<int:pk>/', views.Miniature_APIView_Detail.as_view(), name='MinDetail'),
  path('v1/categories', views.Category_APIView.as_view(), name='Categories'), 
  path('v1/categories/<int:pk>/', views.Category_APIView_Detail.as_view(), name='MinDetail'),
  path('v1/subcategories', views.SubCategory_APIView.as_view(), name='subCategories'), 
  path('v1/subcategories/<int:pk>/', views.SubCategory_APIView_Detail.as_view(), name='MinDetail'),
]