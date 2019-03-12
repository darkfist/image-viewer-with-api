from django.conf.urls import url

from .views import display_images, add_images, image_details, user_images, delete_image


urlpatterns = [
    url(r'^$', display_images, name='view'),
    url(r'^my-images/$', user_images, name='user_img'),
    url(r'^image-details/(?P<slug>[\w-]+)/$', image_details, name='details'),
    url(r'^add/$', add_images, name='add'),
    url(r'^delete/(?P<pk>\d+)/$', delete_image, name='delete'),
]