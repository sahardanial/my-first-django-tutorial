from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^phones/$', views.phone_list, name='phones'),
    url(r'^phones/(?P<pk>\d+)$', views.phone_detail, name='phone-detail'),
    url(r'^costomoptions/$', views.costomoption_list, name='costomoptions'),
    url(r'^costomoptions/(?P<pk>\d+)$', views.costomoption_detail, name='costomoption-detail'),
    url(r'^phonesold$', views.phonesold, name='phonesold'),
]

urlpatterns += [
    url(r'^phones/(?P<pk>\d+)/buy-success$', views.payment, name='payment'),
    url(r'^phones/(?P<pk>\d+)/phone_buy$', views.phone_buy, name='phone_buy'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signup/success$', views.signupsuccess, name='signupsuccess'),
]
