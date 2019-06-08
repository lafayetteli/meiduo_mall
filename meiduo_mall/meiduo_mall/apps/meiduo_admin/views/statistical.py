from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from datetime import date, timedelta
from users.models import User
from rest_framework.response import Response
from goods.models import GoodsVisitCount
from meiduo_admin.serializers.statistical import GoodsSerializer


class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.all().count()
        return Response({
            'count': count,
            'date': now_date
        })


class UserDayCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.filter(date_joined__gte=now_date).count()
        return Response({
            "count": count,
            "date": now_date
        })


class UserActiveCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({
            'count': count,
            'date': now_date
        })


class UserOrderCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        count = User.objects.filter(orders__create_time__gte=now_date).count()
        return Response({
            'count': count,
            'date': now_date,
        })


class UserMonthCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        now_date = date.today()
        start_date = now_date - timedelta(29)
        date_list = []
        for i in range(30):
            index_date = start_date + timedelta(days=i)
            cur_date = start_date + timedelta(days=i + 1)
            count = User.objects.filter(date_joined__gte=index_date, date_joined__lt=cur_date).count()

            date_list.append({
                'count': count,
                'date': index_date
            })

        return Response(date_list)


class GoodsDayView(APIView):
    def get(self, request):
        # 获取当天日期
        now_date = date.today()
        # 获取当天访问的商品分类数量信息
        data = GoodsVisitCount.objects.filter(date=now_date)
        # 序列化返回分类数量
        ser = GoodsSerializer(data, many=True)

        return Response(ser.data)
