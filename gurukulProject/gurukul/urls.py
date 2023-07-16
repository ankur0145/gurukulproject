from django.urls import path
from myapp.views import MyView

urlpatterns = [
    path('my-view/', MyView.as_view(), name='my-view'),
]
