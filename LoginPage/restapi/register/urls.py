from django.conf.urls import url
from django.urls import path
from .views import RegisterCreate,RegisterList,RegisterRetrieve,RegisterDestroy
urlpatterns=[
    path('',RegisterList.as_view()),
    path('create/',RegisterCreate.as_view()),
    url(r'^(?P<pk>\d+)/$',RegisterRetrieve.as_view()),
    url(r'^(?P<pk>\d+)/update/$',RegisterRetrieve.as_view()),
    url(r'^(?P<pk>\d+)/delete/$',RegisterDestroy.as_view())
]
