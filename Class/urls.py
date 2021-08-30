from django.contrib import admin
from django.urls import path
from Class import views
from Class.views import *

urlpatterns = [
    path('',views.index, name='home'),
    path('blogs/',blogs),
    path('Apply/',Apply),
    path('college/',college),
    path('student/',student),
    path('online/',online),
    path('registration/',registration),
    path('About/',About)
]