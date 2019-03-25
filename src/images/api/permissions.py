from rest_framework.permissions import BasePermission

# Custom permissions so that only authenticated users can edit or delete the images
class IsOwnerOrReadOnly(BasePermission):
	message = "Only the owner can update or delete this image."
	my_safe_method = ['GET', 'PUT', 'DELETE']
	def has_permission(self, request, view):
		if request.method in self.my_safe_method:
			return True
		return False

	def has_object_permission(self, request, view, obj):
		if request.method in self.my_safe_method:
			return True
		return obj.uploaded_by == request.user