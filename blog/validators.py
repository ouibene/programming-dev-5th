import re
from django.db import models
from django.forms import ValidationError
import requests
from django.conf import settings
from django.utils.deconstruct import deconstructible
import xmltodict
from django.conf import settings

#우편번호관련
#1번 방법 : open('서울특별시우편번호.csv')
#db model에 넣어서 쓰는 것이 좋을 것

def phone_number_validator(value):
    if not re.match(r'01[06789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')


# def min_length_validator(min_length):
#     def wrap(value):
#         if len(value) < min_length:
#             raise ValidationError('{}글자 이상 입력해주세요.'.format(min_length))
#     return wrap

# def max_length_validator(max_length):
#     def wrap(value):
#         if len(value) > max_length:
#             raise ValidationError('{}글자 미만 입력해주세요.'.format(max_length))
#     return wrap


@deconstructible
class ZipCodeValidator(object):
    def __init__(self, is_check_exist=True):
        self.is_check_exist = is_check_exist

    def __call__(self, zip_code):
        zip_code = str(zip_code)

        if not re.match(r'^\d{5,6}$', zip_code):
            raise ValidationError('5자리 또는 6자리 숫자로 입력해주세요')

        if self.is_check_exist:
            #self.check_exist(zip_code)
            self.check_exist_from_db(zip_code)

    #0803 추가부분
    def check_exist_from_db(self, zip_code):
        from blog.models import Zipcode
        if not Zipcode.objects.filter(code=zip_code).exists():
            raise ValidationError('없는 우편번호입니다.')


    def check_exist(self, zip_code): #이 validator가 call 될 때 마다 매번 들어가서 check를 함
        params = {
            'regkey' : settings.EPOST_API_KEY,
            'target' : 'postNew',
            'query' : zip_code
        }

        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params = params).text
        response = xmltodict.parse(xml)
        try:
            error = response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))