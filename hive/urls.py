from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin


from .views import contactus




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
    url(r'^about$', views.about, name='about'),
    url(r'^solutions$', views.solutions, name='solutions'),
    # url(r'^contact$', views.contact, name='contact'),
    url(r'^solution$', views.solution1, name='solution'),
    url(r'^enterpreneurship$', views.enterpreneurship, name='enterpreurship'), 
    url('contactus/', contactus, name='contactus'),
    url('subscribe/', views.subscribe, name = 'subscribe'),
    url('team/', views.team, name = 'team'),
    url('academics/', views.academics, name = 'academics'),
    url('studentApply/', views.studentApply, name = 'studentApply'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)