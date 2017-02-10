from django.conf.urls import include, url
from django.contrib import admin

from inventory import views
from testing import view


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.articles, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^hello/$', views.hello),
    url(r'^hello_simple/$', views.hello_simple),
    url(r'^hello_template/$', views.hello_template),
    url(r'^hello_class/$', views.HelloTemplate.as_view()),
    url(r'^auth/$', view.auth_view),
    url(r'^login/$', view.login_view),
    url(r'^logged_in/$', view.logged_in_view),
    url(r'^logout/$', view.logout_view),
    url(r'^invalid/$', view.invalid_view),
    url(r'^register/$', view.register_view, name='register'),
    url(r'^registered/$', view.registered_view),
    url(r'^edit_profile/$', view.edit_profile),

    url(r'^inventory/', include('inventory.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
