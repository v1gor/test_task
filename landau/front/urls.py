from django.urls import path

from .views import MainPage, TablePage

urlpatterns = [
    path('', MainPage.as_view()),
    path('tables', TablePage.as_view()),
]
