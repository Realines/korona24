from django.db import models


class SingletonModel(models.Model):
    """Абстрактный класс синглтон-модели"""

    class Meta:
        """Настройки модели"""
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

        # Если нет ни одной записи, возвращаем новый экземпляр.
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
