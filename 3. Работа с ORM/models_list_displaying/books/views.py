from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = "books/books_list.html"
    context = {"books": Book.objects.all().order_by("pub_date")}
    return render(request, template, context)


def date_view(request, date):
    template = "books/date_list.html"
    dates = list(
        Book.objects.values_list("pub_date", flat=True).distinct().order_by("pub_date")
    )
    date_idx = dates.index(datetime.strptime(date, "%Y-%m-%d").date())
    context = {
        "books": Book.objects.filter(pub_date=date).order_by("name"),
        "page": Paginator(list(dates), 1).get_page(date_idx + 1),
        "prev_date": dates[date_idx - 1] if date_idx != 0 else None,
        "next_date": dates[date_idx + 1] if date_idx != len(dates) - 1 else None,
    }
    return render(request, template, context)
