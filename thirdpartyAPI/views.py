# import requests
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class GitHubRepositoriesView(APIView):
#     def get(self, request):
#         access_token = request.query_params.get('access_token')
#         headers = {'Authorization': f'token {access_token}'}
#         url = 'https://api.github.com/swiftv99/repos'
#         response = requests.get(url, headers=headers)
#         repositories = response.json()
#         return Response(repositories)


from django.shortcuts import render
import requests


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