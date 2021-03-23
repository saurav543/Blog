from django.contrib import admin
from .models import Posts,Usercomment


# Register your models here.
admin.site.register(Usercomment)
@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinyinject.js',)
