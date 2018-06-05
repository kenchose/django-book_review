from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^users/(?P<user_id>\d+)$', views.user),
    url(r'^books/add$', views.newAdd),
    url(r'^books/(?P<book_id>\d+)$', views.book),
    url(r'^add$', views.add),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^review/delete/(?P<review_id>\d+)$', views.delete),
    url(r'^delete_confirmation/(?P<review_id>\d+)$', views.confirmation),
    url(r'^logout$', views.logout),
]