
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from .fields import PhoneNumberField
from .validators import phone_number_validator, ZipCodeValidator

from django.core.urlresolvers import reverse

#from .validators import MinLengthvalidator, min_length_validator, lanlat_validator
#min_length_4_validator = MinLengthValidator(4)
#min_length_4_validator = min_length_4_validator(4)

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
    message = models.TextField()
    author = models.CharField(max_length=20)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name





