
from django.contrib import admin
from django.urls import path, include

# from .views import hello

# path может принимать 4 аргумента это:
# обязательные: шаблон url, и функция которая будет обрабатывать запрос по данному шаблону
# имя для паттерна, и доп параметры, которые можно передать функции ввиде словаря
from .views import redirect_blog

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
