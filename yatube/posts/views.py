from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, any_slug):
    return HttpResponse(f'В данном разделе находятся посты')
