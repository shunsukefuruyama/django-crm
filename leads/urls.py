from django.urls import path
from .views import lead_create, lead_list, lead_detail

# this is the namespace defined in the project's url.py
app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('create/', lead_create),
    path('<int:pk>/', lead_detail),

    # Can be accessed at http://127.0.0.1:8000/leads/second_page
    # path('second_page', second_page)
]