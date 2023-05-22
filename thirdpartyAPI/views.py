from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

import requests
from github import Github, GithubException


@permission_classes([IsAuthenticated])
def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'thirdpartyAPI/github.html', {'search_result': search_result})


@permission_classes([IsAuthenticated])
def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        core_rate_limit = rate_limit.core
        search_result['rate'] = {
            'limit': core_rate_limit.limit,
            'remaining': core_rate_limit.remaining,
        }

    return render(request, 'thirdpartyAPI/github.html', {'search_result': search_result})