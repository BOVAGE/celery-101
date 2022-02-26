from django.urls import path
from app2.views import review

app_name = 'app2'
urlpatterns = [
    path('', review, name='review'),
]