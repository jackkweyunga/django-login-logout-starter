
from django.urls import path
import users.views as views

app_name = "users"


urlpatterns = [
    path('add/', views.UserCreateView.as_view(), name="user-add"),
    path('', views.UsersListView.as_view(), name="user-list"),
    path('<pk>/', views.UserDetailView.as_view(), name="user-detail"),
    path('<pk>/delete/', views.UserDeleteView.as_view(), name="user-delete"),
    path('<pk>/update/', views.UserUpdateView.as_view(), name="user-update"),
]

