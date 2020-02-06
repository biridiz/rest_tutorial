from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets import generic_views

urlpatterns = [
    path('snippets/', generic_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', generic_views.SnippetDetail.as_view()),
    path('users/', generic_views.UserList.as_view()),
    path('users/<int:pk>/', generic_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)