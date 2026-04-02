from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from expenses.views import (
    CustomLoginView, CustomLogoutView, RegisterView,
    IncomeListView, IncomeCreateView, IncomeDeleteView,
    ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView
)


urlpatterns = [
    path('admin/',    admin.site.urls),
    path('login/',    CustomLoginView.as_view(),  name='login'),
    path('logout/',   CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(),     name='register'),

    path('expenses/', include('expenses.urls')),
    path('income/',          IncomeListView.as_view(),          name='income-list'),
    path('income/create/',   IncomeCreateView.as_view(),        name='income-create'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
    path('', lambda request: redirect('/expenses/'), name='home'),
]