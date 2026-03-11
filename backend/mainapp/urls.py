from django.urls import path
from .views import index, add_data, get_table

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('add_data/', add_data, name='add-data'),
    path('table/', get_table, name='get-table')
]
