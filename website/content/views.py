from django.views.generic.base import TemplateView
from django.http import HttpResponse
# from db_connection import my_collection


class IndexPage(TemplateView):
    template_name = 'index.html'


class ElysiumPage(TemplateView):
    template_name = 'elysium.html'


class ServicesPage(TemplateView):
    template_name = 'services.html'


class SolutionsPage(TemplateView):
    template_name = 'solutions.html'


# def add_document(request):
#     record = {
#         'id': '2873273827hd7dhbhxhs',
#         'first_name': 'Artem',
#         'last_name': 'Sheptalin',
#     }

#     my_collection.insert_one(record)
#     return HttpResponse('Successfully!')


# def get_all(request):
#     # Получение всех документов из коллекции
#     cursor = my_collection.find()

#     # Преобразование курсора в список документов
#     documents = list(cursor)

#     # Использование шаблона для рендеринга HTML-страницы
#     return HttpResponse(f'{documents}!')




