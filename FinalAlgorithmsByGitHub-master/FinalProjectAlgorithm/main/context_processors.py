from django.urls import resolve
from post.models import CategoryPost


def message_processor(request):
    url_name = resolve(request.path_info).url_name

    if url_name == 'home' or url_name == 'popular_posts':
        num = 1
    elif url_name == 'fresh_posts':
        num = 2
    elif url_name == 'my_subscription':
        num = 3
    else:
        num = 0

    return {
        'page': num
    }