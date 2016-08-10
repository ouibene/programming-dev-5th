from django.conf.urls import url
from django.contrib.auth.views import login
from accounts import views

urlpatterns = [
    url(r'^signup/$', views.signup ),
    url(r'^login/$', login, name = 'login', kwargs={
        "template_name":'accounts/login.html',
        }),
]

# registration/login.html 을 만들거나
# 인자를 바꾼다. 윗 방법은 인자(kwargs)를 바꾸는 방법