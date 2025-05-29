from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView

class ProductPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return self.request.method == 'GET'
        
        if self.request.method == 'DELETE':
            return user.is_staff
            
        return True

    def handle_no_permission(self):
        raise PermissionDenied("You don't have permission to perform this action.") 