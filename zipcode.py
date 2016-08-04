import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings")
import django
django.setup()

import csv


CSV_PATH = "/Users/Youngeun-Lee/Desktop/dev/programming/blog/zipcode/20150710_seoul.txt"
reader = csv.reader(open(CSV_PATH, "rt", encoding="cp949"), delimiter="|")
#이 파일을 읽을 때에 cp949로 encoding한 것을 decoding해라는 뜻

from blog.models import Zipcode

columns = next(reader)

zip_code_list = []


for idx, row in enumerate(reader):
    data = dict(zip(columns, row))
    zip_code = Zipcode(city=data['시도'], road=data['도로명'], dong=data['법정동명'], gu=data['시군구'], code=data['우편번호'])

    #방법0.
    zip_code_list.append(zip_code)
    #방법1. zip_code.save()


#Zipcode.objects.all().delete()

print('zip_code size : {}'.format(len(zip_code_list)))
Zipcode.objects.bulk_create(zip_code_list, 100)
    #print(data [‘우편번호’])
    #if idx>5:
    #break

#print('zip_code size : {}'.format(len()))
#Zipcode.objects.bulk_create(zip_code_list, 100)