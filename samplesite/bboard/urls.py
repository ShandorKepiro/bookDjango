from django.urls import path
from .views import index, by_rubric

urlpatterns = [
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric')
    # <int:rubric_id> угловые скобки помечают описание URL-параметра, языковая конструкция int задает целочисленный тип,
    # а rubric_id - имя параметра контроллера, которому будет присвоено значение этого URL-параметра
    # Созданному маршруту мы сопоставили контроллер-функцию by_rubric()
]
