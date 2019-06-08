from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from users.models import User
from rest_framework.response import Response
from meiduo_admin.utils.pagination import MeiduoPagination
from rest_framework import generics
from meiduo_admin.serializers.users import UserSerializer


# class UserView(APIView):
#     permission_classes = [IsAdminUser]
#     def get(self,reqest):
#         user_list = User.objects.filter(is_staff=False).order_by('-id')
#         serializers = UserSerializers(user_list,many=True)
#         return Response(serializers.data)

# class UserView(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = User.objects.filter(is_staff=False)
#         keyword = self.request.query_params.get('keyword')
#         if keyword:
#             queryset = queryset.filter(username__contains=keyword)
#         queryset.order_by('-id')
#         return queryset
#
#     serializer_class = UserSerializers
#     permission_classes = MeiduoPagination


class UsersView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = User.objects.filter(is_staff=False)
        keyword = self.request.query_params.get('keyword')
        if keyword:
            queryset = queryset.filter(username__contains=keyword)
        queryset = queryset.order_by('-id')
        return queryset

    serializer_class = UserSerializer

    pagination_class = MeiduoPagination
