from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MeiduoPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 10
    page_size_query_param = 'pagesize'

    def get_paginated_response(self, data):
        return Response({
            "counts": self.page.paginator.count,
            "lists": data,
            "page": self.page.number,
            "pages": self.page.paginator.num_pages,
            "pagesize": self.page.paginator.per_page
        })
