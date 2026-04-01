"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse
def landing_page(request):
    return HttpResponse('''
        <html>
        <head><title>OctoFit Tracker API</title></head>
        <body style="font-family:sans-serif; text-align:center; margin-top:10vh; background:linear-gradient(135deg,#f0f4f9,#e0e7ff);">
            <h1 style="color:#1976d2;">Welcome to the OctoFit Tracker API</h1>
            <p style="font-size:1.2em;">Visit <a href="/api/">/api/</a> for available endpoints.</p>
        </body>
        </html>
    ''')
import os

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "http://localhost:8000/api/"
    return JsonResponse({
        "activities": base_url + "activities/",
        "users": base_url + "users/",
        "teams": base_url + "teams/",
        "leaderboard": base_url + "leaderboard/",
        "workouts": base_url + "workouts/",
    })

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('octofit_tracker.urls_api')),
]
