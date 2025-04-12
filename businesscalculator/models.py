from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=63, unique=True, db_index=True, verbose_name="Название")
    year = models.IntegerField(verbose_name="Год основания")
    founder = models.CharField(max_length=63, verbose_name="Основатель")
    country = models.CharField(max_length=31, verbose_name="Страна")
    form = models.CharField(max_length=3, verbose_name="Форма организации")
    industry = models.CharField(max_length=255, verbose_name="Сфера деятельности")
    activity = models.CharField(max_length=255, verbose_name="Основная деятельность")
    registration_date = models.DateField(auto_now_add=True)
    email = models.EmailField(verbose_name="Почта")
    tel = models.CharField(max_length=12, verbose_name="Телефон")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ["-registration_date", "name"]


class Expert(models.Model):
    name = models.CharField(max_length=63, verbose_name="Имя")
    surname = models.CharField(max_length=63, db_index=True, verbose_name="Фамилия")
    last_name = models.CharField(max_length=63, verbose_name="Отчество", blank=True)
    email = models.EmailField(verbose_name="Почта")
    password = models.CharField(max_length=63, default="Null", verbose_name="Пароль")
    city = models.CharField(max_length=63, verbose_name="Город")
    birth_date = models.DateField(verbose_name="Дата рождения")
    registration_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"
        ordering = ["-registration_date", "surname"]



class Balance(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE, verbose_name="Компания")
    date = models.DateField(auto_now_add=True)
    year = models.IntegerField(verbose_name="Отчетный год")
    comment = models.CharField(max_length=255, verbose_name="Комментарий", blank=True)
    current_assets = models.IntegerField(verbose_name="Оборотные активы")
    fixed_assets = models.IntegerField(verbose_name="Внеоборотные активы")
    equity = models.IntegerField(verbose_name="Собственный капитал")
    current_liabilities = models.IntegerField(verbose_name="Текущие обязательства")
    long_liabilities = models.IntegerField(verbose_name="Долгосрочные обязательства")

    def __str__(self):
        return self.company, self.date

    class Meta:
        verbose_name = "Бухгалтерский баланс"
        verbose_name_plural = "Бухгалтерские балансы"
        ordering = ["-date", "company"]


class Statement(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE, verbose_name="Компания")
    date = models.DateField(auto_now_add=True)
    year = models.IntegerField(verbose_name="Отчетный год")
    comment = models.CharField(max_length=255, verbose_name="Комментарий", blank=True)
    revenue = models.IntegerField(verbose_name="Выручка")
    returns = models.IntegerField(verbose_name="Затраты")
    oper_exp = models.IntegerField(verbose_name="Коммерческие расходы")
    other_costs = models.IntegerField(verbose_name="Прочие расходы")
    taxes = models.IntegerField(verbose_name="Налоги")

    def __str__(self):
        return self.company, self.date

    class Meta:
        verbose_name = "Отчет о финансовых результатах"
        verbose_name_plural = "Отчеты о финансовых результатах"
        ordering = ["-date", "company"]


class Report(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE, verbose_name="Компания")
    type_of_report = (
        (True, 'Баланс'),
        (False, 'ОФР')
    )
    select = models.BooleanField(verbose_name='Выбор отчета', choices=type_of_report, max_length=15, default=True)
    comment = models.TextField(max_length=2047, verbose_name="Рекомендации")
    expert = models.ForeignKey("Expert", on_delete=models.CASCADE, verbose_name="Эксперт")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"
        ordering = ["-date", "company"]
