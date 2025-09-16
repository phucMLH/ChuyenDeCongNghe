#Tutorial 2

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#Tutorial 3 + 4

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

#Tutorial 5
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#          views.SnippetList.as_view(),
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          views.SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#          views.SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail'),
# ])


# Tutorial 6
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Router sẽ tự động tạo routes cho ViewSet
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
