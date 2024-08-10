from django.urls import path
from . import views

urlpatterns = [
    path('income/',views.incomeList),
    path('expenses/',views.expensesList),
    path('add_income/',views.addIncome),
    path('add_expense/',views.addExpense),
]