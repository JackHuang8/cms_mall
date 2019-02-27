from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^goods/cate/$', views.GoodsCateView.as_view()),
    url(r'^goods/red/$', views.GoodsRedView.as_view()),
    url(r'^goods/cate_red/$', views.GoodsCate_RedView.as_view()),
    url(r'^goods/list/$', views.GoodsListView.as_view()),
    url(r'^goods/detail/$', views.GoodsDetailView.as_view()),
    url(r'^goods/detail_red//$', views.GoodsDetaiRedlView.as_view()),
    url(r'^goods/add_cart/$', views.GoodsAddCartlView.as_view()),
]
