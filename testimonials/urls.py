from . import views
from django.urls import path


urlpatterns =[
path('',views.tst_view, name = 'tst_view'),
]
