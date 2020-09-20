from rest_framework.permissions import BasePermission



class IsBoardOwner(BasePermission):
	message = "Not Your Board"

	def has_object_permission(self, request, view, obj):
		if obj.owner == request.user:
			return True
		else:
			return False


class IsOwner(BasePermission):
	message = "Not Your Board"

	def has_object_permission(self, request, view, obj):
		if obj.board.owner == request.user:
			return True
		else:
			return False