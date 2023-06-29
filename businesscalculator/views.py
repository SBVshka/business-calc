from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('<h1>Главная страница<h1>')


def about(request):
    return HttpResponse('<h1>О нас</h1>')


def lk(request):
    return HttpResponse('<h1>Личный кабинет пользователя</h1>')


def history(request):
    return HttpResponse('<h1>История проведённых анализов</h1>')

def historyy(request, report_id):
    # if report_id >= max:
    #     raise Http404()
    return HttpResponse(f'<h1>Результаты {report_id}-го анализа</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Извините, но это 404</h1>')