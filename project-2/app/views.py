from app.models import Worker
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_page(request: HttpRequest) -> HttpResponse:
    # worker = Worker(name="", second_name="", salary=50_000)
    # worker.save()
    # Worker.objects.create(name="", second_name="", salary=50_000)

    # Worker.objects.all()
    # Worker.objects.get(id=1)
    # Worker.objects.filter(salary=50_000)

    # worker = Worker.objects.get(id=1)
    # worker.salary = 50_000
    # worker.save()
    # Worker.objects.filter(id=1).update(salary=50_000)

    # Worker.objects.get(id=1).delete()

    return render(request, "index.html")
