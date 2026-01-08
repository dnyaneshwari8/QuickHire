from django.contrib.auth.backends import BaseBackend
from .models import Account

class EmailBackend(BaseBackend):
    """
    Custom backend to login using email only (case-sensitive).
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        try:
            user = Account.objects.get(email=username)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = Account.objects.get(pk=user_id)
            if self.user_can_authenticate(user):
                return user
        except Account.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        """
        Reject inactive users.
        """
        return getattr(user, 'is_active', False)
