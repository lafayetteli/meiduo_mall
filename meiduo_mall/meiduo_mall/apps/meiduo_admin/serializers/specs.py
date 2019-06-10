# from rest_framework import serializers
# from goods.models import SPUSpecification
#
#
# #
# # class SpecsSerialiazers(serializers.Serializer):
# #     id = serializers.IntegerField()
# #     name = serializers.CharField()
# #     spu = serializers.StringRelatedField()
# #     spu_id = serializers.IntegerField()
# #     def create(self, validated_data):
# #         instance = SKUSpecification.objects.create(**validated_data)
# #         return instance
#
#
#
# class SpecsSerialiazers(serializers.ModelSerializer):
#     spu = serializers.StringRelatedField(read_only=True)
#     spu_id = serializers.IntegerField()
#
#     # class Meta:
#     #     modle = SKUSpecification
#     #     filter = '__all__'
#
#     class Meta:
#         model = SPUSpecification  # 商品规格表关联了spu表的外键spu
#         fields = '__all__'
from rest_framework import serializers
from goods.models import SPUSpecification


class SPUSpecificationSerializer(serializers.ModelSerializer):

    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = '__all__'