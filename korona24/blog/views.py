from django.shortcuts import render

from .models import Article


def test(request):
    return render(
        request=request,
        template_name='test.html',
        context={'articles': Article.objects.all()}
    )
