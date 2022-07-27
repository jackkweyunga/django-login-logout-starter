from django.urls import path
import dashboard.views as views

app_name="dashboard"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]