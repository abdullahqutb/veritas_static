from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path("", views.homepage_view, name="homepage"),
  path("team", views.team_view, name="team"),
  path("reports", views.reports_view, name="reports"),
]
