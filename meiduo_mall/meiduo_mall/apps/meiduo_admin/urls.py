from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import statistical,users
urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$',statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$',statistical.UserDayCountView.as_view()),
    url(r'^statistical/day_active/$',statistical.UserActiveCountView.as_view()),
    url(r'^statistical/day_orders/$',statistical.UserOrderCountView.as_view()),
    url(r'^statistical/month_increment/$',statistical.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$',statistical.GoodsDayView.as_view()),
    url(r'^users/$',users.UsersView.as_view()),
]