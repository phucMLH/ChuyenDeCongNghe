from django.http import HttpResponse

def special_case_2003(request):
    return HttpResponse("Special case for year 2003.")

def year_archive(request, year):
    return HttpResponse(f"Year archive: {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Month archive: {year}/{month}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Article detail: {year}/{month}/{slug}")