from django.db import models
import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise forms.ValidationError("Invalid Lanlat Type")

class Post(models.Model):
    author = models.CharField(max_length=20, default='anonymous')
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    tags = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)
    lnglat = models.CharField(max_length=50,
        validators = [lnglat_validator], help_text='위도,경도 포맷으로 입력')