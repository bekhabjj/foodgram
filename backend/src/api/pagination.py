from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """Кастомная пагинация для API.

    Attributes:
        page_size (int): Количество элементов на странице
            по умолчанию.
        page_size_query_param (str): Параметр запроса для
            указания количества элементов на странице.
    """
    page_size = 6
    page_size_query_param = 'limit'
