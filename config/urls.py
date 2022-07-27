
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from dashboard.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', IndexView.as_view()),
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')),
]
