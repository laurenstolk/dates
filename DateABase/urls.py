from django.urls import path
from .views import indexPageView, randDateView, searchDateView, submitDateView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("submitdate", submitDateView, name="submitDate"),
    path("search", searchDateView, name="searchDateABase"),
    path("randomDate", randDateView, name="randomDateGenerator"),
]
