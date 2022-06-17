from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None):
        """Creates and saves a User with the given data
        Args:
            email (str): Given email.
            username (str): Given username.
            password (str, optional): Given password. Defaults to None.
            phone_number (str): Given phone number
        Raises:
            ValueError: In case no email address entered
        Returns:
            obj: User
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )

        user.set_password(password)  # hashes the pwd
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password=None):
        """Creates and saves a superuser with the given data
        Args:
            email (str): Given email.
            username (str): Given username.
            password (str, optional): Given password. Defaults to None.
        Returns:
            obj: Superuser
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


def has_perm(perm):
    """Does the user have a specific permission?"""
    # Simplest possible answer: Yes, always
    return True


class User(AbstractBaseUser):
    """Create table with custom fields in database"""

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=60, default="utilisateur")
    phone_number = models.CharField(max_length=10, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # login_field
    REQUIRED_FIELDS = ["username", "phone_number"]  # pwd is automatically required

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
