from rest_framework import serializers
from goods.models import SPU


class SPUSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


