from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^student$', views.student, name='student'),
    url(r'^freelancer$', views.freelancer, name='freelancer'),
    url(r'^enterprise$', views.enterprise, name='enterprise'),
    url(r'^business$', views.business, name='business'),
    url(r'^academic$', views.academic, name='academic'),
    url(r'^government$', views.government, name='government'),
    url(r'^start$', views.start, name='start'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)