from django.conf.urls import url
from . import views

# cheacks url for put delete and everything
# each route here
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^secret$', views.secret, name="secret"),
    # url(r'^todos/(?P<todo_id>[0-9]+)')
]
