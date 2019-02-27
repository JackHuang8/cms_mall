from django.shortcuts import render

from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView
from redis.client import StrictRedis

from libs.yuntongxun.sms import CCP


class SMSCodeView(APIView):
    def get(self, request, mobile):
        # 获取StrictRedis对象保存数据
        strict_redis = get_redis_connection('sms_codes')  # type:StrictRedis

        # 4、60秒内禁止重复发送短信验证码
        send_flag = strict_redis.get('send_flag_%s' % mobile)
        if send_flag:
            return Response({'message': '发送短信验证码过于频繁'}, status=400)
        # 1、生成短信验证码
        import random
        sms_code = '%06d' % random.randint(0, 999999)
        # 2、使用云通讯发送短信验证码（Celery异步发送短信）
        CCP().send_template_sms(mobile, [sms_code, 5], 1)

        # 3、保存短信验证码（ 设置过期时间）

        strict_redis.setex('sms_%s' % mobile, 5 * 60, sms_code)  # 设置验证码过期时间为5分钟
        strict_redis.setex('send_flag_%s' % mobile, 60, 1)  # 设置短信验证码标识过期时间为1分钟

        # 5、返回响应数据给前端
        return Response({'message': 'ok'})

