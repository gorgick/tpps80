import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import DataJson


def index(request):
    return render(request, 'mainapp/index.html')


def create_model_instances(data_list):
    model_instances = []
    for data in data_list:
        instance = DataJson(
            name=data.get("name"),
            data=data.get("date"),
        )
        model_instances.append(instance)
    print(model_instances)
    return model_instances


def add_data(request):
    if request.POST.get('action') == "post":
        data = json.loads(request.POST.get('data_json'))
        try:
            create_model_instances(data)
            DataJson.objects.bulk_create(create_model_instances(data))
        except Exception:
            print('Error')
        response = JsonResponse({'data': data})
        return response


def get_table(request):
    data_for_table = DataJson.objects.all()
    return render(request, 'mainapp/table.html', {'data_for_table': data_for_table})
