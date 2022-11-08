from django.urls import include, path
from rest_framework import routers

from api.accounts.views import AccountMonthlyView, AccountView

router = routers.DefaultRouter()
router.register(r"monthly", AccountMonthlyView)
router.register(r"", AccountView)

urlpatterns = [
    path("", include(router.urls)),
]
