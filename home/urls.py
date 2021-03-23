from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('',views.home,name="home"),
   path('contact/',views.contact,name='contact'),
   path('about/',views.about,name='about'),
   path('search/',views.search,name="search"),
   path('signUp/',views.signUp,name="signUp"),
   path('signIn/',views.signIn,name="signIn"),
   path('signOut/',views.signOut,name="signOut"),
   path('profile/',views.profile,name="profile"),
]
urlpatterns+=staticfiles_urlpatterns()