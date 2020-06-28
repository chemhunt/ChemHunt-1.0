from django.contrib.auth import views as auth_views
from django.conf.urls import url
from formapp.views import login,auth_view,que1,que2,que3,ans1,ans2,ans3,thanks,logout_request
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$',login),
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^que1/$', que1),
    url(r'^ans1/$', ans1),
    url(r'^que2/$', que2),
    url(r'^ans2/$', ans2),
    url(r'^que3/$', que3),
    url(r'^ans3/$', ans3),
    url(r'^thanks/$', thanks),
    url(r'^logout/$', logout_request)
]