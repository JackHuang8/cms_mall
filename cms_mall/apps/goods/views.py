from django.db.migrations import serializer
from django.http import HttpResponse

#
# a = 111
# def test(request):
#     return HttpResponse('test',a)
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

#GET /goods/cate/
import goods
from goods import serializers
from goods.models import GoodsCategory, Goods

# http://127.0.0.1:8000/goods/cate/
class GoodsCateView(APIView):
    '''商品类别视图'''


    def get(self,request):
        #查询所有的一级分类
        category_queryset = GoodsCategory.objects.filter(parent_id=0)
        data_list = []
        #遍历一级分类获取二级分类：
        for category in category_queryset:
            # 一级分类字典
            category_dict = serializers.GoodsCategorySerializer(category).data
            # 二级分类
            s_category = category.goodscategory_set.all()
            # 二级分类id列表
            ids_list = []
            for cate in s_category:
                ids_list.append(cate.id)

            #　分类商品表
            category_dict['goods'] = serializers.GoodsSerializer(Goods.objects.filter(category_id__in=ids_list).order_by('-create_time')[0:5], many=True).data
            data_list.append(category_dict)

        return Response(data_list)


#http://127.0.0.1:8000/goods/red
class GoodsRedView(APIView):
    '''商品推荐'''
    def get(self,request):
    #     goods_queryset = Goods.objects.filter(is_red=1).exclude(img_url="").order_by('-sales')[0:4]
    #     # 遍历要推荐商品查询集,获得每个推荐商品对象
    #     # goodre_list = []
    #
    #     # for goodre in goods_queryset:
    #     #     goodre_dict = serializers.GoodsSerializer(goodre).data
    #     #     print(goodre_dict)
    #     #     goodre_dict['id'] = serializers.GoodsSerializer(goodre.id).data
    #     #     goodre_dict['title'] = serializers.GoodsSerializer(goodre.title).data
    #     #     goodre_dict['img_url'] = serializers.GoodsSerializer(goodre.img_url).data
    #     #     goodre_dict['create_time'] = serializers.GoodsSerializer(goodre.create_time).data
    #     #     goodre_list.append(goodre_dict)
    #     return Response(goodre_list)
    # queryset= Goods.objects.filter(is_red=1).exclude(img_url="").order_by('-sales')[0:4]
    # serializer_class = serializers.GoodsSerializer
        goods_queryset = Goods.objects.filter(is_red=1).exclude(img_url="").order_by('-sales')[0:4]

        data = serializers.GoodsSerializer(goods_queryset,many=True).data
        return Response(data)

class GoodsCate_RedView(APIView):
    pass


class GoodsListView(APIView):
    pass




class GoodsDetailView(APIView):
    pass


class GoodsDetaiRedlView(APIView):

    pass


class GoodsAddCartlView(APIView):
    pass