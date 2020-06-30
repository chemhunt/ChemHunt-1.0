from django.contrib.auth import views as auth_views
from django.conf.urls import url
from formapp.views import login,auth_view,que,ans,thanks,logout_request,export_xls,bulk_add_users
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$',login),
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    # url(r'^que1/$', que1),
    # url(r'^ans1/$', ans1),
    # url(r'^que2/$', que2),
    # url(r'^ans2/$', ans2),
    url(r'^que/$', que),
    url(r'^ans/$', ans),
    url(r'^thanks/$', thanks),
    url(r'^logout/$', logout_request),
    url(r'^xls/$', export_xls, name='export_xls'),
    url(r'^read_data/$', bulk_add_users),
]