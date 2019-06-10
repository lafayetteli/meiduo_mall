from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from meiduo_admin.serializers.specs import SPUSpecificationSerializer
from goods.models import SPUSpecification
from meiduo_admin.utils.pagination import MeiduoPagination



# class SpecsView(ModelViewSet):
#
#     serializer_class = SpecsSerialiazers
#     queryset = SKUSpecification.objects.all()
#     pagination_class = MeiduoPagination
#
# class SpecsView(generics.ListAPIView):
#     serializer_class = SPUSpecificationSerializer
#     queryset = SPUSpecification.objects.all()
#     pagination_class = MeiduoPagination
#
# class SpecView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SPUSpecificationSerializer
#     queryset = SPUSpecification.objects.all()

class SpecsView(ModelViewSet):
    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = MeiduoPagination
