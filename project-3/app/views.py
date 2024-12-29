from app.models import Worker
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_page(request: HttpRequest) -> HttpResponse:
    context = {"workers": Worker.objects.all()}

    return render(request, "index.html", context)
