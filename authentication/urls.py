from django.conf.urls import url

from authentication.views import IndexView

app_name = "authentication"

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index"),
]
