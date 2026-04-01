from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from expenses.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth URLs
    path('login/',    LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',   LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    # Expense URLs
    path('expenses/', include('expenses.urls')),
]