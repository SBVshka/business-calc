from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.functions.datetime import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *


def index(request):
    return render(request, 'businesscalculator/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'businesscalculator/about.html', {'title': 'О сайте'})


@login_required
def lk(request, nick):
    companies = Company.objects.filter(user__username=nick).order_by('pk')
    return render(request, 'businesscalculator/lk.html', {'companies': companies, 'title': 'Личный кабинет'})


def gallery(request):
    experts = Expert.objects.all().order_by('pk')
    return render(request, 'businesscalculator/gallery.html', {'experts': experts, 'title': 'Галерея экспертов'})


@login_required
def companynumber(request, pk):
    companies = Company.objects.filter(pk=pk)
    return render(request, 'businesscalculator/company.html',
                  {'companies': companies, 'title': 'Информация о компании'})


@login_required
def history(request, username):
    isit = year_now - 1
    if request.GET:
        print(request.GET)
    balance_reports = Balance.objects.filter(company__user__username=username).order_by('year')
    statement_reports = Statement.objects.filter(company__user__username=username).order_by('year')
    return render(request, 'businesscalculator/history.html',
                  {'balance_reports': balance_reports, 'statement_reports': statement_reports,
                   'title': 'История проведённых исследований', 'isit': isit})


@login_required
def balance_report(request, company, report_id):
    balance_report_object = Balance.objects.filter(company=company, year=report_id)
    year = report_id + 1
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    report = Report.objects.filter(company=company, date__gt=start_date, date__lt=end_date, select=True)
    if request.GET:
        print(request.GET)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Главная страница')
    else:
        form = CommentForm()
    return render(request, 'businesscalculator/balance_report.html',
                  {'form': form, 'balance_report_object': balance_report_object, 'report': report, 'title': 'Анализ '
                                                                                                            'баланса'})


@login_required
def statement_report(request, company, report_id):
    statement_report = Statement.objects.filter(company=company, year=report_id)
    year = report_id + 1
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    report = Report.objects.filter(company=company, date__gt=start_date, date__lt=end_date, select=False)
    if request.GET:
        print(request.GET)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Главная страница')
    else:
        form = CommentForm()
    return render(request, 'businesscalculator/statement_report.html',
                  {'form': form, 'report': report, 'statement_report': statement_report, 'title': 'Анализ ОФР'})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Извините, но это 404</h1>')


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'businesscalculator/company_data.html'
    form_class = CompanyDataForm
    success_url = reverse_lazy('Главная страница')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = 'businesscalculator/company_data.html'
    form_class = CompanyDataForm
    success_url = reverse_lazy('Главная страница')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user:
            return self.handle_no_permission()
        return kwargs


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'businesscalculator/delete.html'
    success_url = reverse_lazy('Главная страница')


class BalanceCreateView(LoginRequiredMixin, CreateView):
    model = Balance
    template_name = 'businesscalculator/balance_sheet.html'
    form_class = BalanceDataForm
    success_url = reverse_lazy('Главная страница')


class StatementCreateView(LoginRequiredMixin, CreateView):
    model = Statement
    template_name = 'businesscalculator/statement.html'
    form_class = StatementForm
    success_url = reverse_lazy('Главная страница')


class Registration(View):
    template_name = 'registration.html'

    def get(self, request):
        context = {
            'form': RegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password, email=email, last_name=last_name,
                                first_name=first_name)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
