from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^users$',views.showRegister),    
    url(r'^register$',views.register),
]
