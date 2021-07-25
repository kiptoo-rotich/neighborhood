from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('add_post/',views.add_post,name='add_post'),
    path('businesses/',views.businesses,name='businesses'),
    path('post_chat/',views.post_chat,name='post_chat')
]