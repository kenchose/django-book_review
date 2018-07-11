from django.conf.urls import url
from django.contrib import admin  
from . import views
# from django.conf import settings  look up about static imports
# from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^edit/(?P<user_id>\d+)$', views.edit_user),
    url(r'^edit_profile/(?P<user_id>\d+)$', views.update_user),
    url(r'^books/add$', views.newAdd),
    url(r'^books/(?P<book_id>\d+)$', views.book),
    url(r'^add$', views.add),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^review/delete/(?P<review_id>\d+)$', views.delete),
    url(r'^delete_confirmation/(?P<review_id>\d+)$', views.confirmation),
    url(r'^logout$', views.logout),
] 