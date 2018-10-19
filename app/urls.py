from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
       url(r'^$',views.home,name='Home'),
       url(r'^new_project',views.new_project,name='new_project'),
       url(r'^new/profile$', views.new_profile, name='new-profile'),
       url(r'^profile/',views.profile, name='profile'),
       url(r'^rate/(\d+)$',views.rating,name='rating'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
