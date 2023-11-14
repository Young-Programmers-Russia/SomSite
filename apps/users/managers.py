from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


def salt_encoded_from_id(user_id, shift):
    salt = ''

    for i in user_id:
        shifted_word = ord(i) + shift
        salt = salt + chr(shifted_word)

    return salt


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_("User must have an username"))

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        salt = salt_encoded_from_id(str(user.id), 1)

        user.password = make_password(password, salt)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
