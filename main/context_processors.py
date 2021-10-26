from django.urls import reverse


def urls_list(request):
    return {"nav_urls": (
        ("О проекте", reverse("about")),
        ("Главная", reverse("index")),
        ("Минчане на карте Минска", reverse("streets"))
    )}
