from django.urls import path
from .views import GitHubRepositoriesView

urlpatterns = [
    path('github/repositories/', GitHubRepositoriesView.as_view(), name='github-repositories'),
    # Other URLs...
]
