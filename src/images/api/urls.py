from django.conf.urls import url

from .views import (
	ImageCreateAPIView,
	ImageListAPIView,
	ImageDetailAPIView,
	ImageUpdateAPIView,
	ImageDeleteAPIView
	)


urlpatterns = [
	url(r'^$', ImageListAPIView.as_view(), name='view'),
    url(r'^create/$', ImageCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ImageDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', ImageUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ImageDeleteAPIView.as_view(), name='delete'),
]