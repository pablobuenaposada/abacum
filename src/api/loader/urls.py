from django.urls import path

from api.loader import views

urlpatterns = [path("", views.LoadFileView.as_view())]
