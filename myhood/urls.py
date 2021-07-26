from django.urls import path,include

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('add_post/',views.add_post,name='add_post'),
    path('businesses/',views.businesses,name='businesses'),
    path('post_chat/',views.post_chat,name='post_chat'),
    path('accounts/profile/<id>',views.profile,name='profile'),
    path('update/',views.updateprofile,name = 'updateprofile'),
    path('business/<int:id>',views.single_business,name='business'),
    path('neighbor/',views.neighbor,name='neighbor'),
    path('search',views.search,name='search'),
]