from rest_framework import serializers
from goods.models import SKU,SKUSpecification
from django.db import transaction

class SKUSpecificationSerialzier(serializers.ModelSerializer):
    spec_id = serializers.IntegerField(read_only=True)
    option_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SKUSpecification
        fields = ("spec_id", 'option_id')

class SKUGoodsSerialzier(serializers.ModelSerializer):
    specs = SKUSpecificationSerialzier(read_only=True,many=True)
    category_id = serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    spu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SKU
        fields = '__all__'

    def update(self, instance, validated_data):
        specs = self.context['request'].data.get('specs')
        with transaction.atomic():
            sid = transaction.savepoint()
            try:
                sku = super().create(validated_data)
                for itam in specs:
                    itam['sku_id'] = sku.id
                    SKUSpecification.objects.create(**itam)
            except:
                transaction.savepoint_rollback(sid)
                raise serializers.ValidationError('更新失败')
            else:
                transaction.savepoint_commit(sid)

        

