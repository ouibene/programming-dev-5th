"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from pokemon import views as pokemon_views #pokemon에서 view를 import하는데 pokemon_views로써(이름을 이것으로) import하겠다.

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),
    url(r'^profile/', views.profile),

#정규표현식 연습. 항상 패턴이 맞아야 호출된다.
    url(r'^sum2/(?P<x>[\d/]+)/$', views.mysum2), #\d는 0-9까지, /는 슬래시 1개 포함해서. 1회 이상이라는 뜻.

    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/$', views.mysum),

    url(r'^pokemon/$', pokemon_views.pokemon_list),

    url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comment/(?P<pk>\d+)/edit/$', views.comment_edit),

    url(r'^post_detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post_new/(?P<pk>\d+)/$', views.post_new, name='post_new'),


    url(r'^accounts/', include('accounts.urls')), #accounts는 namespace를 붙이지 않는다. include이므로 $를 붙이지 않음.

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)