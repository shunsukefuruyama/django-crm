from django.contrib import admin
from django.urls import path, include
# from leads.views import home_page, second_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),

    # When template folder is under the project
    # Need to configure DIRS of TEMPLATES in settings.py
    # Can be accessed at http://127.0.0.1:8000/second_page
    # path('second_page', second_page)
]
