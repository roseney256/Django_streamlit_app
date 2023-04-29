from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, firstname, secondname, password=None):
        if not email:
            raise ValueError("Users must enter a valid Email address")
        if not username:
            raise ValueError("Users must enter a username")
        if not firstname:
            raise ValueError("Users must enter a Firstname")
        if not secondname:
            raise ValueError("Users must enter a Secondname")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            secondname=secondname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, firstname, secondname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            secondname=secondname,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'secondname']

    objects = MyAccountManager()

    def __str__(self):
        return self.firstname
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
