from .views import *

from django.urls import path, include

urlpatterns = [
    path('', index, name='Главная страница'),
    path('about/', about, name='О нас'),
    path('lk/<slug:nick>/', lk, name='Личный кабинет'),
    path('history/<slug:username>/', history),
    path('history/balance_report/<int:company>/<int:report_id>/', balance_report),
    path('history/statement_report/<int:company>/<int:report_id>/', statement_report),
    path('registration/', Registration.as_view()),
    path('company_data/', CompanyCreateView.as_view()),
    path('company_data/<int:pk>/', CompanyUpdateView.as_view()),
    path('company_delete/<int:pk>/', CompanyDeleteView.as_view()),
    path('balance_sheet/', BalanceCreateView.as_view()),
    path('statement/', StatementCreateView.as_view()),
    path('au/', include('django.contrib.auth.urls')),
    path('company/<int:pk>/', companynumber),
    path('gallery/', gallery),
]
