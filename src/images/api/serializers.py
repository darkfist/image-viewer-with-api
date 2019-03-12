from rest_framework.serializers import ModelSerializer, SerializerMethodField
from images.models import Image


class ImageCreateSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
			'image',
			'uploaded_by',
		]


class ImageListSerializer(ModelSerializer):
	image = SerializerMethodField()
	uploaded_by = SerializerMethodField()
	class Meta:
		model = Image
		fields = [
			'id',
			'title',
			'description',
			'image',
			'uploaded_by',
		]
	def get_uploaded_by(self, obj):
		return str(obj.uploaded_by.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image


class ImageDetailSerializer(ModelSerializer):
	image = SerializerMethodField()
	uploaded_by = SerializerMethodField()
	class Meta:
		model = Image
		fields = [
			'id',
			'title',
			'description',
			'image',
			'uploaded_by',
		]
	def get_uploaded_by(self, obj):
		return str(obj.uploaded_by.username)

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image


class ImageUpdateSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
		]