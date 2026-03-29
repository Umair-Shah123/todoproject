from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("update/<int:id>/",views.update_task,name='updated_task'),
     path("delete/<int:id>/",views.delete_task,name='delete_task')
]