from rest_framework import serializers

from goods.models import GoodsCategory, Goods


class GoodsCategorySerializer(serializers.ModelSerializer):
    '''商品类别序列化器'''

    class Meta:
        model = GoodsCategory
        fields = ('id', 'title', 'parent_id', 'sort_id')


class GoodsSerializer(serializers.ModelSerializer):
    '''商品类别序列化器'''

    class Meta:
        model = Goods
        fields = ('id', 'title', 'img_url', 'sell_price', 'market_price', 'sub_title', 'stock')
