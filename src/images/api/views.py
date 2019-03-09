from  rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from images.models import Image
from .serializers import PostListSerializer, PostDetailSerializer, PostUpdateSerializer

class ImageListAPIView(ListAPIView):
	queryset = Image.objects.all()
	serializer_class = PostListSerializer

class ImageDetailAPIView(RetrieveAPIView):
	queryset = Image.objects.all()
	serializer_class = PostDetailSerializer
	# lookup_field = 'uploaded_by'
	# lookup_url_kwarg = 'user'

class ImageUpdateAPIView(UpdateAPIView):
	queryset = Image.objects.all()
	serializer_class = PostUpdateSerializer
	# def get_serializer_class(self):
	# 	if self.request.user.is_staff:
	# 		return FullAccountSerializer
	# 	return BasicAccountSerializer

class ImageDeleteAPIView(DestroyAPIView):
	queryset = Image.objects.all()
	serializer_class = PostDetailSerializer