# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page1story/', views.page1story, name='page1story'),
    path('page1/', views.page1, name='page1'),
    path('page2story/', views.page2story, name='page2story'),
    path('page2/', views.page2, name='page2'),
    path('page3story/', views.page3story, name='page3story'),
    path('page3/', views.page3, name='page3'),
    path('page4story/', views.page4story, name='page4story'),
    path('page4/', views.page4, name='page4'),
    path('page5story/', views.page5story, name='page5story'),
    path('page5/', views.page5, name='page5'),
    path('page6story/', views.page6story, name='page6story'),
    path('page6/', views.page6, name='page6'),
    path('page7story/', views.page7story, name='page7story'),
    path('page7/', views.page7, name='page7'),
    path('page8story/', views.page8story, name='page8story'),
    path('page8/', views.page8, name='page8'),
    path('page9story/', views.page9story, name='page9story'),
    path('page9/', views.page9, name='page9'),
    path('last_page/', views.last_page, name='last_page'),
    path('reset_choices/', views.reset_choices, name='reset_choices'),
]
