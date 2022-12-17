from rest_framework.pagination import PageNumberPagination

#para esta app esta va a ser la configuración de paginación
class SimplePagination(PageNumberPagination):
    page_size = 50
    page_query_param = "page_size"
    max_page_size = 2000