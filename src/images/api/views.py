from django.db.models import Q
from rest_framework.generics import (
			CreateAPIView,
			ListAPIView,
			RetrieveAPIView,
			RetrieveUpdateAPIView,
			DestroyAPIView
			)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from images.models import Image
from .serializers import (
			ImageCreateSerializer,
			ImageListSerializer,
			ImageDetailSerializer,
			ImageUpdateSerializer
			)

from .permissions import IsOwnerOrReadOnly # custom permission


class ImageCreateAPIView(CreateAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageCreateSerializer


class ImageListAPIView(ListAPIView):
	serializer_class = ImageListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset_list = Image.objects.all()
		query1 = self.request.GET.get("id")
		if query1:
			queryset_list = queryset_list.filter(Q(id__icontains=query1)).distinct()
		query2 = self.request.GET.get("user")
		print (query2)
		if query2:
			queryset_list = queryset_list.filter(Q(uploaded_by__username=query2)).distinct()
		return queryset_list


class ImageDetailAPIView(RetrieveAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageDetailSerializer
	

class ImageUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ImageDeleteAPIView(DestroyAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageDetailSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]