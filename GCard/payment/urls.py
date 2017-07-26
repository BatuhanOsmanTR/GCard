from django.conf.urls import url
from payment.views import *

urlpatterns = [
    url(r"^$", hView.as_view(), name="home"),
    url(r"^detail/(?P<pk>d+)-(?P<slug>[A-Za-z0-9\-]+)$", pDetail.as_view(), name="product_detail"),
    url(r"^card/(?P<slug>[A-Za-z0-9\-]+)$", card.as_view(), name="card_detail"),
    url(r"^balance/", balance.as_view(), name="balance"),]

