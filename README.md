# Бизнес-калькулятор

Веб-приложение, которое предназначено для помощи представителям малого и среднего бизнеса с разрешенем многочисленных вопросов и сложностей, возникающих при проведении анализа основных и обязательных для всех компаний форм отчётности: бухгалтерского баланса и отчёта о финансовых результатах (отчёта о прибылях и убытках).

Помощь планируется осуществлять за счёт консультаций опытных экспертов, которые будут проводить анализ данных, внесённых пользовтелем, формировать список рекомендаций о потенциально возможных управленческих решениях и прикреплять полученный перечень к ранее созданному отчёту. 

Что касается внесения предпринимателями данных, то мы постарались максимально упростить этот нелёгкий процесс, разработав три осноные формы, которые призваны, во-первых, сделать более понятной для пользователей работу с сайтом, а во-вторых, снизить количество ввода невалидной информации и передачи ошибочного ТЗ экспертам. Такое решение, на наш взгляд, способно повысить эффективность проведения анализа форм отчётности и уменьшить риск выполнения сотрудниками лишней работы, связанной с установлением корректности полученной информации. Подробнее о формах будет рассказано далее.

Кроме того, у нас есть две странцы, на которых будет отображаться история вводимых пользователем данных, редактировать их можно перейдя непосредственно к конкретному отчёту при помощи специальной кнопки.

Теперь чуть подробнее постараемся раскрыть каждый элемент нашего веб-приложения, рассказав о том, как он был реализован. Если в данной пояснительной записке мы что-то упустили, то готовы с радостью ответить на дополнительные вопросы во время защиты проекта.

<h2>Основные разделы веб-приложения</h2>

Наше веб-приложение состоит из нескольких разделов, премещение между которыми осуществляется при помощи меню, расположенном в заголовке на каждой странице. Предлагаем отдельно остановиться на каждом элементе.

<h3>Загловок</h3>

Является одним из основных элементов сайта, в котором расположены:

1. Меню, включающее ссылки на: главную страницу, личный кабинет, историю отчётов, галерею экспертов, все три формы;
2. Кнопка регистрации (для неавторизированных пользователей);
3. Кнопка авторизации (для неавторизированных пользователей);
4. Кнопка выхода из учётной записи (для авторизированных пользователей).

Файл, где можно найти код для данного элемента: header.html

<img src="/businesscalculator/static/businesscalculator/for_report/header.png">

<h3>Подвал</h3>

Является одним из основных элементов сайта, в котором расположены:

1. Краткое описание идеи веб-приложения;
2. Полезные для пользователей разделы веб-приложения;
3. Ссылки на полезные для дополнительного изучения внешние ресурсы;
4. Copyright.

Файл, где можно найти код для данного элемента: footer.html

<img src="/businesscalculator/static/businesscalculator/for_report/footer.png">

<h3>Базовый шаблон</h3>

Включает в себя заголовок и подвал, а также блок контента. Служит в качестве основы для всех остальных шаблонов веб-приложения.

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
    <title>{{ title }}</title>
</head>
<body>
    {% include 'businesscalculator/header.html' %}

    {% block content %}
    {% endblock %}

    {% include 'businesscalculator/footer.html' %}
</body>
</html>
```

Файл, где можно найти код для данного элемента: base.html

<h3>Главная страница</h3>

Является стартовой страницей, с которой начинается знакомство пользователя с нашим веб-приложением. Призвана объяснить новым гостям сайта, что они могут получить в процессе взаимодействия с ним. Также здесь расположены ссылки на формы для внесения данных с целью получения отчётов от экспертов.

Файл, где можно найти код для данного элемента: index.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/index.png">

<h3>Личный кабинет</h3>

Представляет собой страницу, где выводится основная информация (предоставляющая возможность идентифицировать конкретную организацию) о тех компаниях, которые когда-либо добавлял определённый пользователь. Они выводятся в виде некого списка. Рядом с каждой записью есть кнопка, позволяющая перейти на форму для просмотра и изменения всех введённых ранее данных.

Файл, где можно найти код для данного элемента: lk.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/lk.png">

<h3>История отчётов</h3>

Представляет собой страницу, где выводится основная информация (предоставляющая возможность идентифицировать конкретную формц отчётности) о тех формах отчётности, которые были ранее добавлены пользователем. Данные представлены в виде списка. Рядом с каждой записью есть кнопка, позволяющая перейти на форму для просмотра и изменения всех введённых ранее данных. 

Кроме того, добавлена возможность различать Баланс и Отчёт о финансовых результатах при помощи цвета кнопки и значка (синий vs зелёный).

Файл, где можно найти код для данного элемента: lk.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/history.png">

<h3>О нашем проекте</h3>

Здесь представлена информация об участиках проекта, их зонах ответсвенности, процессе выбора темы для веб-приложения и благодарности организаторам курса.

Файл, где можно найти код для данного элемента: about.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/about.png">

<h3>Внести данные бухгалтерского баланса</h3>

Здесь расположена форма, которая позволяет пользователю внести значения основых разделов бухгалтерского баланса, используемые впоследствие экспертами для формирования управленческих решений, необходимых комапнии. После нажатия кнопки "Добавить" данные отправляются POST-запросом на сервер.

Файл, где можно найти код для данного элемента: balance_sheet.html _(представляет собой расширение типовой формы (type_form.html))_

<img src="/businesscalculator/static/businesscalculator/for_report/balance_sheet.png">

<h3>Внести данные отчёта о финансовых результатах</h3>

Здесь расположена форма, которая позволяет пользователю внести значения ключевых элементов отчёта о финансовых результатах, используемые впоследствие экспертами для формирования управленческих решений, необходимых компании. После нажатия кнопки "Добавить" данные отправляются POST-запросом на сервер.

Введённые данные можно найти, перейдя со страницы "История отчётов" на описание конкретной компании.

Файл, где можно найти код для данного элемента: statement.html _(представляет собой расширение типовой формы (type_form.html))_

<img src="/businesscalculator/static/businesscalculator/for_report/statement.png">

<h3>Ввести данные о компании</h3>

Здесь расположена форма, которая позволяет пользователю внести ключевую информацию о компании, используемые впоследствие экспертами для формирования управленческих решений, необходимых организации. После нажатия кнопки "Добавить" данные отправляются POST-запросом на сервер.

Введённые данные можно найти, перейдя со страницы "Личный кабинет" на описание конкретной компании.

Файл, где можно найти код для данного элемента: company_data.html _(представляет собой расширение типовой формы (type_form.html))_

<img src="/businesscalculator/static/businesscalculator/for_report/company_data.png">

<h3>Галерея экспертов</h3>

На данной странице расположена вся информация об экспертах, которые будут давать оценку формам годовой отчётности компаний, в том числе: ФИО, дата рождения, город и адрес электронной почты для обратной связи.

Файл, где можно найти код для данного элемента: gallery.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/gallery.png">

<h3>Регистрация</h3>

На данной странице расположена форма, которая позволяет новому пользователю зарегистрироваться на сайте посредством внесения основных данных о себе.

Файл, где можно найти код для данного элемента: registration.html _(представляет собой расширение типовой формы (type_form.html))_

<img src="/businesscalculator/static/businesscalculator/for_report/registration.png">


<h3>Войти</h3>

На данной странице расположена форма, которая позволяет авторизироваться ранее авторизированному пользователю.

<img src="/businesscalculator/static/businesscalculator/for_report/login.png">

<h3>Информация о компании</h3>

На данной странице расположена вся введённая ранее информация о компании, которую ввёл пользователь. Кроме того, тут расположена кнопка, при нажатии на которую у предпринимателя появляется возможность изменить некоторые данные о компании.

Файл, где можно найти код для данного элемента: gallery.html _(представляет собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/company.png">

<h3>Анализ баланса / Анализ ОФР</h3>

На данной странице расположена вся введённая ранее информация о бухгалтерском балансе (отчёте о финансовых результатах), которую ввёл пользователь. Кроме того, тут расположены таблицв с данными о компании и форма, позволяющая экспертам оставлять комментарии по форме отчётности.

Файлы, где можно найти код для данного элемента: balance_report.html и statement_report.html _(представляют собой расширение базового)_

<img src="/businesscalculator/static/businesscalculator/for_report/balance_report.png">

<h2>Реализация CRUD подхода</h2>

<h3>Create</h3>

Для того, чтобы внести информацию о компании или формах отчётности в базу данных, пользователь может воспользоваться разработанными нами для трёх моделей формами. Для этих целей в файле views.py находятся класса.

1. CompanyCreateView - позволяет внести данные о новой компании

```python
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
```

2. BalanceCreateView - позволяет внести данные бухгалтерского баланса

```python
class BalanceCreateView(LoginRequiredMixin, CreateView):
    model = Balance
    template_name = 'businesscalculator/balance_sheet.html'
    form_class = BalanceDataForm
    success_url = reverse_lazy('Главная страница')
```

3. StatementCreateView - позволяет внести данные отчёта о финансовых результатах

```python
class StatementCreateView(LoginRequiredMixin, CreateView):
    model = Statement
    template_name = 'businesscalculator/statement.html'
    form_class = StatementForm
    success_url = reverse_lazy('Главная страница')
```

<h3>Read</h3>

Чтение данных происходит за счёт запроса к БД, к примеру: statement_report = Statement.objects.filter(year=report_id)

<h3>Update</h3>

Для того чтобы обновить данные о зарегистрированной ранее в приложении пользователем организации, он может воспользоваться кнопкой "Внести изменения" на странице с краткой информацией о ней. Произойдёт переход на шаблон с формой, где будут содержаться актуальные данные с сервера. Отредактировав некоторые значения, пользователь отправляет обновлённую информацию в БД.

Для этих целей служит класс CompanyUpdateView.

```python
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
```

Было принято решение не добавлять возможность обновления данных о формах отчётности, потому что подобные действия пользователя могут поставить под сомнение работу экспертов. К примеру, анализ уже был проведён, однако клиент решил изменить исходную информацию, что сделало труд сотрудика напрасным.

<h3>Delete</h3>

Решили, что возможность удаления данных из БД тоже также стоит добавить только для компаний по той же самой причине.

Для этих целей служит класс CompanyDeleteView.

```python
class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'businesscalculator/delete.html'
    success_url = reverse_lazy('Главная страница')
```

<h3>Плюс</h3>

Кроме того, существует класс для формы регистрации, где прописаны отдельно прописаны функции get и post - Registration.

```python
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
```

А также есть функции balance_report и statement_report, которые отвечают за вывод информации об отчётности компании за определённый год и содержат форму для написания комментариев. В качестве примера приведу одну из них:

```python
def balance_report(request, report_id):
    balance_report_object = Balance.objects.filter(year=report_id)
    year = report_id + 1
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    report = Report.objects.filter(date__gt=start_date, date__lt=end_date, select=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/history/')
    else:
        form = CommentForm()
    return render(request, 'businesscalculator/balance_report.html',
                  {'form': form, 'balance_report_object': balance_report_object, 'report': report, 'title': 'Анализ баланса'})
```

<h2>Не существует страницы</h2>

Если какой-то страницы не существует, то пользователь будет перенаправлен на страницу 404. Реализуется это при помощи слудующей функции из файла views.py:

```python
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Извините, но это 404</h1>')
```

В urls.py также есть строка, которая связана с данной функцией:

```python
handler404 = page_not_found
```

Дизайн страницы довольно прост, поскольку не нашли большого смысла над ним стараться.

<h2>Валидация в формах</h2>

Реализована валидация данных в формах. Если пользователь попробует отправить данные, которые не соответсвуют установленному формату, то получит ошибку. Информация на сервер не уйдёт. 

Пример:

Поле form модели Company должно содержать максимум 3 буквы:

```python
form = models.CharField(max_length=3, verbose_name="Форма организации")
```

Соответственно, пользователь не сможет отправить данные с 4-мя и более символами. А также отсутсвует возможность заполнить поле цифрами.

Поскольку для каждой формы в файле forms.py задана модель, от которой были взяты правила проверки данных, то их лучше искать в models.py.

Важно отметить, что в файле views.py прописан метод is_valid(), который возвращает True, если данные корректны, и False - если данные некорректны. Тем самым припятствует отправки некорркетных данных на сервер. К примеру, в представленной ранее функции balance_report:

```python
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/history/')
```

<h2>Проверка входных параметров</h2>

Помимо того функционала, который предлагает Django по проверке входных данных на корректность на стороне серверной логики, нами были доработаны доп проверки.
К примеру, функция, контролирующая правильность передаваемой информации о годе основания компании:

```python
def clean_year(self):
    year = self.cleaned_data['year']
        if year > year_now:
            print('error')
            raise ValidationError('Вы из будущего что ли?:)')
        return year
```

<h2>Процесс авторизации и регистрации</h2>

Нами был реализован процесс регистрации пользователей при помощи специальной формы, куда гость веб-приложения заносит основные данные о себе, а именно:

1. Имя;
2. Фамилия;
3. Адрес электронной почты;
4. Ник нейм;
5. Пароль (два раза)

Класс формы можно найти в файле forms.py и выглядит он следующим образом:

```python
class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ivan_ivanov'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов'}),
            'form': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ПАО'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ivanova94@mail.ru'}),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Надёжный'}),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ещё раз надёжный'})
        }
```

Также у нас есть специально написанная для этих целей view, где содержаться две функции: get и post. Выглядит она следующим образом:

```python
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
```

Также можно ознакомится с шаблоном регистрации, но он является типовым, то есть расширением от type_form.html

Хочется отметить, что в случае реализации процесса регистрации мы воспользовались тем функционалом, который предоставляет Django, к примеру, модель - User, поскольку тех данных, что пользователь даёт нам сейчас, достаточно, чтобы идентифицировать его.

Процесс авторизации также был реализован, но уже при помощи django.contrib.auth.urls. Поэтому, нажав на кнопку "Войти", пользователь попадает на страницу с url http://127.0.0.1:8000/au/login/, где ему доступна классическая форма входа. После успешной авторизации гость сайта попадает вновь на главную страницу.

Чтобы выйти из своей учётной записи пользователю нужно нажать на кнопку "Выйти", которая становится доступна лишь после успешной авторизации. 

Что касается ограничения возможностей для неавторизированных пользователей, то в нашем веб-приложении данный функционал был реализован. 

Во-первых, гости, не прошедшие регистрацию, не смогут перейти на большинство страниц. Им будут доступны лишь:

1. Главная страница
2. О нашем проекте
3. Галерея экспертов

Реализовано это было довольно тривиальным способом, а именно при помощи простейшего условия:

```python
{% if user.is_authenticated %}
#something
{% else %}
#something else
{% endif %}
```

Во-вторых, неавторизированные пользователи не смогут создать, обновить или удалить информацию, поскольку в соответсвующих классах есть наследование от LoginRequiredMixin, который был импортирован из django.contrib.auth.mixins.

<h2>Часть HTML/CSS кода</h2>

Здесь постарались сделать всё в соответствии со сформированными требованиями:

1. не был использован атрибут style;
2. не использовался !important;
3. идентификатор вроде бы используются по назначению;
4. форматирование исходного кода выполнено при помощи отступов (хотя где-то могли упустить этот момент)
5. используется селектор лоботомированной совы.

С шаблонами можно поподробнее познакомится, перейдя в папку templates. Их предназначение описано выше в части "Основные разделы веб-приложения" 

<h2>Требования к наименованию переменных</h2>

Все требования были нами соблюдены, а именно:

1. Наименования переменных отражают их суть;
2. Наименования переменных написаны без использования транслитераций;
3. Наименования переменных не содержат орфографических ошибок (чего нельзя сказать об этой записке);
4. Был выбран единый стиль для оформления наименований переменных.

<h2>Что касается urls.py</h2>

Если открыть файл businesscalc/urls.py, то там помимо классического для django кода можно найти:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('businesscalculator.urls')),
]
```

Перейдя в файл businesscalculator/urls.py, можно найти следующую маршрутизацию:

```python
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
    path('company_data/<int:pk>/', CompanyDeleteView.as_view()),
    path('balance_sheet/', BalanceCreateView.as_view()),
    path('statement/', StatementCreateView.as_view()),
    path('au/', include('django.contrib.auth.urls')),
    path('company/<int:pk>/', companynumber),
    path('gallery/', gallery),
]
```

Все использованные выше названия отражают основную суть получаемых url, поэтому остановка на каждом из них не имеет большого смысла.

<h2>Модели</h2>

<h3>Компания</h3>

| Поле | Характеристика | Особенности |
| ------ | ------ | ------ |
| id | Идентификатор компании | Уникальное значение, число |
| name | Название компании | Максимальная длина = 63 символа, значение уникальное, строка |
| year | Год основания | Число |
| founder | Основатель | Максимальная длина = 63 символа, строка |
| country | Страна | Максимальная длина = 31 символ, строка |
| form | Форма организации | Максимальная длина = 3 символа, строка |
| industry | Отрасль | Максимальная длина = 255 символов, строка |
| activity | Основной вид деятельности | Максимальная длина = 255 символов, строка |
| registration_date | Дата регистрации в приложении | Проставляется автоматически, дата |
| email | Адрес электронной почты |  |
| tel | Телефон | Максимальная длина = 12 символов, строка |
| user | Пользователь | Внениий ключ на модель пользователя |

Пример кода:

```python
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
```

<h3>Эксперт</h3>

| Поле | Характеристика | Особенности |
| ------ | ------ | ------ |
| id | Идентификатор эксперта | Уникальное значение, число |
| name | Имя | Максимальная длина = 63 символа, строка |
| surname | Фамилия | Максимальная длина = 63 символа, строка |
| last_name | Отчество | Максимальная длина = 63 символа, строка, может быть пустым |
| email | Адрес электронной почты |  |
| password | Пароль | Максимальная длина = 63 символа, строка, по умолчанию - null |
| city | Город | Максимальная длина = 63 символа, строка |
| birth_date | Дата рождения | Дата |
| registration_date | Дата регистрации в приложении | Проставляется автоматически, дата |

Пример кода:

```python
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
```

<h3>Баланс</h3>

| Поле | Характеристика | Особенности |
| ------ | ------ | ------ |
| id | Идентификатор баланса | Уникальное значение, число |
| company | Идентификатор компании | Внешний ключ на модель Компания |
| date | Дата внесения данных о форме отчётности | Проставляется автоматически, дата |
| year | Отчётный период | Число |
| comment | Комментарий от пользователя | Максимальная длина = 255 символов, строка, по умолчанию - null |
| current_assets | Оборотные активы | Число |
| fixed_assets | Внеоборотные активы | Число |
| equity | Капитал и резервы | Число |
| current_liabilities | Краткосрочные обязательства | Число |
| long_liabilities | Долгосрочные обязательства | Число |

Пример кода:

```python
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
```

<h3>Отчёт о финансовых результатах</h3>

| Поле | Характеристика | Особенности |
| ------ | ------ | ------ |
| id | Идентификатор ОФР | Уникальное значение, число |
| company | Идентификатор компании | Внешний ключ на модель Компания |
| date | Дата внесения данных о форме отчётности | Проставляется автоматически, дата |
| year | Отчётный период | Число |
| comment | Комментарий от пользователя | Максимальная длина = 255 символов, строка, по умолчанию - null |
| revenue | Выручка | Число |
| returns | Затраты | Число |
| oper_exp | Коммерческие расходы | Число |
| other_costs | Прочие расходы | Число |
| taxes | Налоги | Число |

Пример кода:

```python
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
```

<h3>Комментарий</h3>

| Поле | Характеристика | Особенности |
| ------ | ------ | ------ |
| id | Идентификатор комментария | Уникальное значение, число |
| company | Идентификатор компании | Внешний ключ на модель Компания |
| type_of_report | Тип отчёта | Булево |
| select | Выбор отчёта | Булево |
| comment | Рекомендации | Максимальная длина = 2047, текст |
| expert | Эксперт | Внешний ключ на модель Эксперт |
| date | Дата составления отчёта | Проставляется автоматически, дата |

Пример кода:

```python
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
```


