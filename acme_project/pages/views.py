# pages/views.py

from django.views.generic import TemplateView

from birthday.models import Birthday

from django.contrib.auth import get_user_model


class HomePage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста из родительского метода.
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь ключ total_count;
        # значение ключа — число объектов модели Birthday.
        context['total_count'] = Birthday.objects.count()

        # Получаем модель, зарегистрированную в конфиге проекта,
        # в константе AUTH_USER_MODEL
        User = get_user_model()

        # И в коде применяем значение переменной User, 
        # которое вернула функция get_user_model():
        users = User.objects.all()
        context['users'] = users

        user = self.request.user
        user.refresh_from_db()
        print(user.username)
        print(user.user_permissions.all())

        # Возвращаем изменённый словарь контекста.
        return context
