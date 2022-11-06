from django.urls import include, path

urlpatterns = [
    path("loader/", include("api.loader.urls")),
    path("accounts/", include("api.accounts.urls")),
]
