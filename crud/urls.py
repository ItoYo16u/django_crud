from django.urls import path
from . import views

app_name='crud'
urlpatterns=[
    path('',views.index,name="index"),
    path('show/<int:id>/',views.show,name="show"),
    path('create/',views.create,name="create"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('download/<int:id>/',views.download,name="download"),
    path('download_all/',views.download_all,name="download_all"),
]