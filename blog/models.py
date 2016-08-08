
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from .fields import PhoneNumberField
from .validators import phone_number_validator, ZipCodeValidator

from django.core.urlresolvers import reverse

import os
from uuid import uuid4
from django.utils import timezone

from django.core.files import File
from django.db.models.signals import pre_save
from programming.pil_image import thumbnail

#from .validators import MinLengthvalidator, min_length_validator, lanlat_validator
#min_length_4_validator = MinLengthValidator(4)
#min_length_4_validator = min_length_4_validator(4)

#db처리는 여기서 처리하는게 일관된 처리이다.
def myupload_to(instance, filename): #중간 경로와 최종파일명까지를 기대하게된다. 문자열로 리턴해야.
    #만일 return 'blog/post/20160808/start.jpg'라면 계속 여기에만 저장된다.
        # post = instance
        # filename
        # return 'blog/post/20160808/'+filename
    #확장자를 지키고 싶을 때
        # os.path.splitext(filename)[-1]
        # return 'blog/post/20160808/'+filename
    #랜덤으로 만들고 싶을 때 16^3개의 dir이 존재
    #name[6:]과 extension 사이에 comma는 넣지 않는다. (확장자가 파일명이 되므로)
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join(name[:3], name[3:6], name[6:] + extension)
    #pass



@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length=min_length

    def __call__(self,value):
        if len(value) < self.min_length:
            raise ValidationError("{}글자 이상 입력해주세요".format(self.min_length))


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise forms.ValidationError("Invalid Lanlat Type")


#validators= [blog.validators.MinLengthValidator(10)]
class Post(models.Model):
    author = models.CharField(max_length=20, default='anonymous')
    title = models.CharField(max_length=100, verbose_name='제목', validators= [MinLengthValidator(2)])
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    #tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10, blank=True)
    lnglat = models.CharField(max_length=50,
        validators = [lnglat_validator], help_text='위도,경도 포맷으로 입력')
    tag_set = models.ManyToManyField('Tag', blank=True)
    phone = models.CharField(max_length=20, validators = [phone_number_validator], blank=True)
    photo = models.ImageField(blank=True, upload_to = myupload_to) #default로 '' (빈 문자열)을 주거나, 경로를 주어도 된다.


# 아래 코드(함수)는 주소를 만들어주는 것. reverse. 이렇게 쓰면
# view에서 쓴 코드

#     return render(request, 'blog/post_detail.html', {
#         'form':form,
#         })

# 를 단순하게 return redirect(post)라고 쓸 수 있다.

    def get_absolute_url(self):
        return reverse('blog.views.post_detail', args=[self.pk])

    def __str__(self):
        return self.title

    @property
    def lat(self):
        return self.lnglat.split(',')[1]

    @property #property의 용도는?
    def lng(self):
        return self.lnglat.split(',')[0]



class Zipcode(models.Model):
    #api를 이용할 때
    #zipcode = models.IntegerField(validators = [ZipCodeValidator()])

    #csv파일을 이용할 때
    city = models.CharField(max_length=20, blank=True)
    road = models.CharField(max_length=20, blank=True)
    dong = models.CharField(max_length=20, blank=True)
    gu = models.CharField(max_length=20, blank=True)
    code  = models.CharField(max_length=7, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number1 = PhoneNumberField()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    jjal = models.ImageField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


def on_pre_save(sender, **kwargs):
    post = kwargs['instance']
    if post.photo : #경로가 있다면 이라는 의미. 이미지가 있다는 것과는 다른 개념.
        #print(post.photo.path) #경로가 있다면 저장되기 직전 path 출력.
        max_size = 300
        if post.photo.width > max_size or post.photo.height > max_size:
            processed_file = thumbnail(post.photo.file, max_size, max_size) #max_size, max_size는 가로 세로 사이즈를 의미
            post.photo.save(post.photo.name, File(processed_file)) #파일을 바꾸기 위함이지 파일명을 바꾸는 것이 아니므로.

#함수를 연결하는데 저장되기 직전에 on_pre_save. connect함수는 DB에 연결해주는 함수.
pre_save.connect(on_pre_save, sender=Post)

