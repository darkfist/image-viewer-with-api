from rest_framework.serializers import ModelSerializer
from images.models import Image

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			'title',
			'description',
			'img_url',
			'uploaded_by',
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'id',
			'title',
			'description',
			'img_url',
			'uploaded_by',
		]

class PostUpdateSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
		]