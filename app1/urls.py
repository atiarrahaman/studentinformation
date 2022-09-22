from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:id>',views.Delete_data , name='delete'),
    path('<int:id>',views.edit_data , name='edit'),
    path('details/<int:id>',views.details_data , name='details'),
    path('singup',views.singup , name='singup'),
]
