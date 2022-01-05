from django.core import paginator
from rest_framework import pagination
from django.core.paginator import Paginator

class CustomPagination(Paginator):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 3
    page_query_param = 'p'