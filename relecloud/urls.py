## APP (relecoud) 

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('inicio', views.index, name='index'),
    path('about', views.about, name='about'),
    path('reviews', views.reviews, name='reviews'),
    #Creamos el path de info/<int:destination_id> para que nos lleve a la info de cada destination
    path('new_review', views.new_review, name='new_review'),
    path('info/<int:destination_id>', views.info, name='info'),
    path('info_request', views.info_request, name='info_request'),
    path('new_info_request', views.new_info_request, name='new_info_request'),
]
