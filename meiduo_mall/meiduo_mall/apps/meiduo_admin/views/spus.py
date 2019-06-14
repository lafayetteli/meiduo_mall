from rest_framework import generics
from meiduo_admin.serializers.spus import SPUSerializers
from goods.models import SPU

class SPUSimpleViwe(generics.ListAPIView):
    serializer_class = SPUSerializers
    queryset = SPU.objects.all()