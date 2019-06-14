from rest_framework.viewsets import ModelViewSet
from meiduo_admin.serializers.skus import SKUSpecificationSerialzier
from goods.models import SKU
from django.db.models import Q
from meiduo_admin.utils.pagination import MeiduoPagination


class SKUGoodsView(ModelViewSet):
    serializer_class = SKUSpecificationSerialzier
    pagination_class = MeiduoPagination

    def get_queryset(self):
        queryset = SKU.objects

        keyword = self.request.query_params.get('keyword')
        if keyword:
            queryset = queryset.filter(Q(name__contains=keyword) | Q(caption__contains=keyword))

        queryset = queryset.order_by('-id')
        return queryset
        # return queryset

        #
        # queryset = SKU.objects
        #
        # keyword = self.request.query_params.get('keyword')
        # if keyword:
        #      queryset = queryset.filter(Q(name__contains=keyword) | Q(caption__contains=keyword))

        # queryset = queryset.order_by('-id')
        # return queryset
