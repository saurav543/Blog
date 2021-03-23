from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('usercomment/',views.usercomment,name="usercomment"),
   path('',views.bloghome,name="bloghome"),
   path('<str:slug>',views.blogpost,name="blogpost"),
]
urlpatterns+=staticfiles_urlpatterns()
