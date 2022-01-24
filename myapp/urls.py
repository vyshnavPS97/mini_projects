from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^indexes$', views.index),
    url(r'^logins$', views.logins),
    url(r'^registers$', views.registers),
    url(r'^home2$', views.home),
    url(r'^signup$', views.signup),
    url(r'^signin$', views.signin),
    url(r'^logout$', views.logout),
    url(r'^placeorders$', views.placeorder),
    url(r'^orders$', views.order),
    url(r'^payments$', views.payment),
    url(r'^payeds$', views.payed),
    url(r'^myorder$', views.myorder),
    url(r'^show$', views.show_order_details),
    url(r'^deletes/(?P<item_id>\d+)$', views.delete),
    url(r'^edit/(?P<item_id>\d+)$', views.edit),
    url(r'^update/(?P<item_id>\d+)$', views.update),
    url(r'^searched$', views.search),
    url(r'^about$', views.aboutus),
    url(r'^drinks$', views.drinks),
]