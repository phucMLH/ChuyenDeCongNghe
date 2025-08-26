from django.http import HttpResponse

def special_case_2003(request):
    return HttpResponse("Special case for year 2003.")

def year_archive(request, year):
    return HttpResponse(f"Year archive: {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Month archive: {year}/{month}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Article detail: {year}/{month}/{slug}")

import datetime
from django.http import Http404
from django.core.exceptions import PermissionDenied

def current_datetime(request):
    now = datetime.datetime.now()
    html = f'<html lang="en"><body>It is now {now}.</body></html>'
    return HttpResponse(html)

def not_found_view(request):
    raise Http404("This page does not exist")

def permission_denied_view(request):
    raise PermissionDenied

def created_view(request):
    return HttpResponse("Created!", status=201)

async def async_current_datetime(request):
    now = datetime.datetime.now()
    html = f'<html lang="en"><body>It is now {now}.</body></html>'
    return HttpResponse(html)

from django.shortcuts import render
def example_template_view(request):
    books = Book.objects.all()
    context = {
        'name': 'John Doe',
        'today': datetime.datetime.now(),
        'books': books,
    }
    return render(request, 'polls/example.html', context)

def example_outside_template_view(request):
    context = {'name': 'Jane Doe'}
    return render(request, 'example_outside.html', context)

# Class-based views
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Book
import asyncio

class AboutView(TemplateView):
    template_name = "about.html"


class BookListView(ListView):
    model = Book
    def head(self, *args, **kwargs):
        # Giả sử Book có trường published_year kiểu datetime
        last_book = self.get_queryset().latest("published_year")
        response = HttpResponse(
            headers={
                "Last-Modified": last_book.published_year.strftime("%a, %d %b %Y %H:%M:%S GMT")
            },
        )
        return response


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")