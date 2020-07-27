from django.urls import path
from myapp import views

app_name="myapp"#is used to give the namespace to the urls of the app
#not mandatory to use app_name

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
    #path('secondarysuffix',address of function,name of mapping) 
    path('parent',views.parent,name='parent'), 
    path('child',views.child,name='child'),  
]