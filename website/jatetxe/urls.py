from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('sukaldariak/', views.sukaldariak, name='sukaldariak'),
    path('platerak/<price>', views.platerak, name='platerak'),

    path('platerak/reset/', views.reset, name='reset'),

    path('delsukaldari/<int:id>', views.delsukaldari, name='delsukaldari'),
    path('delplatera/<int:id>', views.delplatera, name='delplatera'),

    path('addsukaldari/', views.addsukaldari, name='addsukaldari'),
    path('addplatera/', views.addplatera, name='addplatera'),

    path('addsukaldari/addsukaldaritodb/', views.addsukaldaritodb, name='addsukaldaritodb'),
    path('addplatera/addplateratodb/', views.addplateratodb, name='addplateratodb'),

    path('updatesukaldari/<int:id>', views.updatesukaldari, name='updatesukaldari'),
    path('updateplatera/<int:id>', views.updateplatera, name='updateplatera'),

    path('updatesukaldari/updatesukaldariondb/<int:id>', views.updatesukaldariondb, name='updatesukaldariondb'),
    path('updateplatera/updateplateraondb/<int:id>', views.updateplateraondb, name='updateplateraondb'),
    
    

]