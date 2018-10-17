from django.conf.urls import url

from . import views
urlpatterns=[
       url(r'^$',views.home,name='Home'),
       url(r'^new_project',views.new_project,name='new_project'),
]
