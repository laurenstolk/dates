from django.urls import path
from .views import deleteDateView, indexPageView, sendUpdatePage, randDateView, updateDatePageView, saveDateView, searchDateView, submitDateView, showDatesViews


urlpatterns = [
    path("", indexPageView, name="index"),
    path("submitdate/", submitDateView, name="submitDate"),
    path("search/", searchDateView, name="searchDate"),
    path("randomDate/", randDateView, name="randomDateGenerator"),
    path("updateDate/<int:date_id>/", updateDatePageView, name="updateDate"),
    path("showDates/", showDatesViews, name="showDates"),
    path("saveDate/", saveDateView, name="saveDate"),
    path("sendupdateDate/", sendUpdatePage, name="sendupdateDate"),
    path("deleteDate/<int:date_id>/", deleteDateView, name="deleteDate"),
]
