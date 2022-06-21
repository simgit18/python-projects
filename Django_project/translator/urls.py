from . import views
from django.urls import path

urlpatterns = [

    path('', views.TranslatorView, name='translator_views')

]