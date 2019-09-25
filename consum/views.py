from django.shortcuts import render
import requests

# def home(request):
#     response = requests.get('https://mannu-awards.herokuapp.com/api/profiles/')
#     profiles = response.json()
#     return render(request, 'core/home.html', {
#         'email': profiles['email']
#     })

def home(request):
    # url = 'https://api.github.com/users/%s'
    url = ('https://mannu-awards.herokuapp.com/api/projects/')
    response = requests.get(url)
    email = response.json()
    return render(request, 'core/home.html', {'email': email})