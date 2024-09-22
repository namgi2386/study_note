from django.urls import path
from . import views

app_name = "tempapp"

urlpatterns = [
    path('',views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    # path('crt/',views.crt, name='crt'),
    path('<work>/',views.detail, name='detail'),
]
