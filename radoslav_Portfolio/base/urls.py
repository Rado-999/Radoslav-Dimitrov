from django.urls import path

from radoslav_Portfolio.base import views

urlpatterns = (
    path('', views.homepage, name='home'),
)