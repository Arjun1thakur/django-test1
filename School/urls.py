from django.contrib import admin
from django.urls import path, include

admin.site.site_header="AJ INSTITUTE OF TECHNOLOGY TEACHER LOGIN"
admin.site.site_title="AJ INSTITUTE ADMIN PORTAL"
admin.site.index_title="Welcome to AJ INSTITUTE"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Class.urls'))
]