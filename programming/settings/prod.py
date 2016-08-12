from .common import *

#debug, allowed_hosts, database 이 세가지는 꼭 필요하다.

DEBUG = False
#debug true로 해놓으면 메모리가 계속 쌓이게 된다. 그러면 메모리가 부족해져서 서버다운 - 서버가 응답을 못하는 상황이 됨.

ALLOWED_HOSTS = ['*']
#모든 도메인을 허용하겠다는 의미.

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'ubuntu',
        'USER':'ubuntu',
        'PASSWORD':'withaskdjango!',
        'HOST':'127.0.0.1',
    },
}
#127.0.0.1 은 자기자신을 의미