from django.forms import ModelForm
from .models import Consultation


class ConsultationForm(ModelForm):
    """Форма для удобной валидации данных для консультации"""

    class Meta:
        """Класс настроек формы"""
        model = Consultation
        fields = ('client_name', 'phone_number')
