from django.urls import path
from crud_app import views

app_name = "crud_app"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='musician_update'),
    path('musician_delete/<pk>/', views.DeleteMusician.as_view(), name='musician_delete'),
    
]
