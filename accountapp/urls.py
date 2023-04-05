from django.urls import path
from accountapp.views import main

app_name = 'accountapp'
accountapp:main

urlpatterns = [
    path('main/',main,name='main'),
]
