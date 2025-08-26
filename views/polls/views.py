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