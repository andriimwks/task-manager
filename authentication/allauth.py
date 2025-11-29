from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from allauth.account.adapter import DefaultAccountAdapter


User = get_user_model()


class AccountAdapter(DefaultAccountAdapter):
    def send_password_reset_mail(self, user: User, email: str, context):
        if settings.DEBUG:
            return messages.warning(
                self.request,
                mark_safe(
                    '<a href="%s">Password reset link</a>'
                    % context["password_reset_url"]
                ),
            )

        return super().send_password_reset_mail(user, email, context)
