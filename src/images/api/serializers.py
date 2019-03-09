from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from images.models import Image


image_url = HyperlinkedIdentityField(view_name = 'images:details', lookup_field = 'slug')

class PostListSerializer(ModelSerializer):
	url = image_url
	uploaded_by = SerializerMethodField()
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
			'url',
			'uploaded_by',
		]
	def get_uploaded_by(self, obj):
		return str(obj.uploaded_by.username)


class PostDetailSerializer(ModelSerializer):
	url = image_url
	uploaded_by = SerializerMethodField()
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
			'url',
			'uploaded_by',
		]
	def get_uploaded_by(self, obj):
		return str(obj.uploaded_by.username)


class PostUpdateSerializer(ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'title',
			'description',
		]