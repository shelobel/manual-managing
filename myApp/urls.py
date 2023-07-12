from django.contrib import admin  
from django.urls import path  
from . import views  
urlpatterns = [  
    path('', views.home, name = 'home'),
    path('add_manual/', views.manual_add ,name = 'add_manual'),  
    path('edit/<int:id>/', views.edit, name = 'edit'),  
    path('update/<int:id>/', views.update, name = 'update'),  
    path('delete/<int:id>/', views.destroy, name = 'delete'),  
]  
# urlpatterns = [
#     path('', views.home, name = 'home'),
#     path('about/',views.about),
#     # path('add_material/<str:primaryKey>/',views.add_material, name = 'add_material'),
#     # path('materials/<str:primaryKey>/',views.material, name = "materials"),
# ]
