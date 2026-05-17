from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    return JsonResponse({
        "message": "Notes Management API is running!",
        "version": "1.0.0",
        "endpoints": {
            "register": "/api/auth/register/",
            "login": "/api/auth/login/",
            "token_refresh": "/api/auth/token/refresh/",
            "notes": "/api/notes/",
            "note_detail": "/api/notes/<id>/",
        }
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
]
