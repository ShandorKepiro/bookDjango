from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    # Заголовок объявления. CharField строковое поле фиксированной длины
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    # Сам текст объявления, описание товара. TextField текстовое поле неограниченной длины или memo-поле.
    # Присвоив параметрам null и blank конструктора значение True, мы указываем, что поле можно не заполнять
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    # Цена. Поле для хранения вещественных чисел. Также необязательно к заполнению
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    # класс ForeignKey представляет поле внешнего ключа, в котором фактически будет храниться ключ записи из первичной моде

    # Дата публикации. Поле для хранения временной отметки. auto_now_add = true - мы предписываем django указывать
    # текущие дату и время
    # Параметр db_index = True указывает создать для этого поля индекс
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']
        # verbose_name_plural - название модели в множественном числе
        # verbose_name = название модели в единственном числе
        # ordering - последовательность полей, по которым по умолчанию будет выполняться сортировка полей


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
