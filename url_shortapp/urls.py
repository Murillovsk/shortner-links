from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("validate_link/", views.validate_link, name="validate_link"),  # type: ignore
    path('<str:link>', views.redirecion, name='redirecion'),
]
