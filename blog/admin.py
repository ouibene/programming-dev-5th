from django.contrib import admin
from blog.models import Post, Tag, Contact, Zipcode, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin): #custom ModelAdmin
    list_display = ['id', 'title', 'content']

class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'city', 'dong', 'gu', 'road']



admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(Zipcode, ZipcodeAdmin)
admin.site.register(Comment)