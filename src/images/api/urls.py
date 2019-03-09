from django.conf.urls import url

from .views import ImageListAPIView, ImageDetailAPIView, ImageUpdateAPIView, ImageDeleteAPIView


urlpatterns = [
    url(r'^$', ImageListAPIView.as_view(), name='view'),
    url(r'^(?P<pk>\d+)/$', ImageDetailAPIView.as_view(), name='details'),
    # url(r'^(?P<user>[\w-]+)/$', ImageDetailAPIView.as_view(), name='details'),
    url(r'^(?P<pk>\d+)/edit/$', ImageUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ImageDeleteAPIView.as_view(), name='delete'),
    # url(r'^add/$', add_images, name='add'),
]