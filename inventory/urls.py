from django.conf.urls import url, include
from inventory import views

urlpatterns = [
	url(r'^all/$', views.articles),
	url(r'^get/(?P<inventory_id>\d+)/$', views.article),
	url(r'^language/(?P<lang>[a-z\-]+)/$',views.language),
	url(r'^create/$', views.create),
	url(r'^add_comment/(?P<inventory_id>\d+)/$', views.add_comment),
	url(r'^like/(?P<inventory_id>\d+)/$', views.like),

]