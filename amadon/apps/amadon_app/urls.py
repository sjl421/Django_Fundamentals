from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'buy/$', views.buy), #no ^ because default to amadon/ in the beginning
    url(r'checkout/$', views.checkout),
    url(r'reset/$', views.reset),
]
