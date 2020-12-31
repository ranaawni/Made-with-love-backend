
from .views import getCategoryItems
from .views import orderItem
from django.urls import path
from django.urls import include, re_path
from .views import payment
# from .views import checkOutItem
# ---> add here the rest of the url 
# path('', signupSeller.as_view(),)

urlpatterns = [
    path('order', orderItem.as_view(), ),
    path('<slug:cat>', getCategoryItems.as_view(), ),
    path(r'^test-payment/$', payment.as_view(),),
    # path('checkout', checkOutItem.as_view(),)

 ]