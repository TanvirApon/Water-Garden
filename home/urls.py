from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='about'),
    path("fishes/",views.fishes,name='fishes'),
    path("contact/",views.contact,name='contact'),
    path("aqurium/",views.aqurium,name='aqurium'),
    path("food/",views.food,name='food'),
    path("order/",views.order,name='order'),
    path("products/<int:myid>",views.product,name='products'),
    path("fishview/<int:myid>",views.fishview,name='fishview'),
    path("foodview/<int:myid>",views.foodview,name='foodview'),
]