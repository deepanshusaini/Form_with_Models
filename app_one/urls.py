from django.urls import path
from app_one import views

app_name = 'app_one'


urlpatterns = [
    path('form/',views.forms,name='form'),

]


