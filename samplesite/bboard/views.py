from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import BbForm
from .models import Bb, Rubric
from django.views.generic.edit import CreateView


def index(request):
    # s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.order_by('-published')
    # return HttpResponse(template.render(context, request))
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubric': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    # Контроллер-класс делаем производным от CreateView. Базовый класс знает, как создать форму,
    # вывести на экран страницу с применением указанного шаблона.
    template_name = 'bboard/create.html'  # путь к файлу шаблона, создающего страницу с формой
    form_class = BbForm  # ссылка на класс формы, связанной с моделью
    success_url = reverse_lazy('index')  # интернет-адрес для перенаправления после успешного сохранения данных
    #  reverse_lazy() из django.urls принимает имя маршрута и значения всех входящих в маршрут URL-параметров.

    def get_context_data(self, **kwargs):
        # kwargs - произвольное число именованных элементов. При вызове функции, на его место передается список
        # именованных аргументов, заключенных в словарь
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
