from django.urls import path
from .views import IndexPage, ElysiumPage, ServicesPage, SolutionsPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('elysium/', ElysiumPage.as_view(), name='elysium'),
    path('services/', ServicesPage.as_view(), name='services'),
    path('solutions/', SolutionsPage.as_view(), name='solutions'),
    # path('all/', get_all, name='all'),
    # path('add/', add_document, name='add'),
]