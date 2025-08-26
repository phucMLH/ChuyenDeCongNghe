from django.urls import path
from . import views

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
    path("now/", views.current_datetime, name="current_datetime"),
    path("notfound/", views.not_found_view, name="not_found"),
    path("forbidden/", views.permission_denied_view, name="forbidden"),
    path("created/", views.created_view, name="created"),
    path("asyncnow/", views.async_current_datetime, name="async_current_datetime"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("asyncview/", views.AsyncView.as_view(), name="async_view"),
    path("template-example/", views.example_template_view, name="template_example"),
    path("outside-template/", views.example_outside_template_view, name="outside_template"),
]
