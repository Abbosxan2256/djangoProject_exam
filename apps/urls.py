from django.urls import path

from apps.views import index_veiw

urlpatterns = [
    path('', index_veiw, name='index_veiw'),
]
