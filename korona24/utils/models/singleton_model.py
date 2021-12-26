from django.db import models
from django.contrib import admin
from django.db.utils import ProgrammingError


class SingletonModel(models.Model):
    """Абстрактный класс синглтон-модели"""

    class Meta:
        """Настройки модели"""
        # Эта модель будет абстрактной, т.е. таблица в БД
        # создаваться не будет.
        abstract = True

    def save(self, *args, **kwargs):
        """Метод сохранения записи в БД"""

        # При сохранении удаляем все записи, кроме вновь созданной.
        # Таким образом будет происходить "обновление" данных даже
        # при попытке создать новую запись.
        # Конструкция self.__class__ используется потому, что мы
        # обращаемся к менеджеру объектов модели. Модель будет наследовать
        # переопределенный метод save и вместо self.__class__ будет подставляться
        # класс, который унаследовал SingletonModel и который вызывает save.
        self.__class__.objects.exclude(pk=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Метод загрузки единственно экземпляра модели"""

        # Если нет ни одной записи, возвращаем новый пустой экземпляр.
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SingletonModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        """Инициализатор класса"""
        super().__init__(model, admin_site)

        # Создаем дефолтный экземпляр модели при первом запросе.
        try:
            model.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        """
        Метод проверки прав на добавление.
        По умолчанию запрещаем добавление новых записей.
        """
        return False

    def has_delete_permission(self, request, obj=None):
        """
        Метод проверки прав на удаление.
        По умолчанию запрещаем удаление записей.
        """
        return False

