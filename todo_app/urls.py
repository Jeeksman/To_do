from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.result,name='result'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tkview/',views.Taskview.as_view(),name='tkview'),
    path('tkdview/<int:pk>',views.Taskdetailview.as_view(),name='tkdview'),
    path('tkupdate/<int:pk>',views.Taskupdateview.as_view(),name='tkupdate'),
    path('tkdelete/<int:pk>',views.Taskdeleteview.as_view(),name='tkdelete')
]