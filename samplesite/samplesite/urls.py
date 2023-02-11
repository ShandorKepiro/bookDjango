from django.contrib import admin
from django.urls import path, include
# from bboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('bboard.urls'))

]
