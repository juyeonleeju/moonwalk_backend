from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, user_ID, email, name, password=None):
        if not user_ID:
            raise ValueError('아이디를 꼭 적어주세요')
        user = self.model(
            user_ID=user_ID,
            email=self.normalize_email(email),
            name=name,
            #User_ID=User_ID,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_ID, email, name, password):
        user = self.create_user(
            user_ID=user_ID,
            email=email,
            name=name,
            password=password,
        )

class User(AbstractBaseUser):
    user_ID = models.CharField(null=True,max_length = 500, unique=True,)
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        #unique=True,
    )
    name = models.CharField(max_length=30) #실명
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True,auto_now_add = True) #추가
    updated_at = models.DateTimeField(null=True,auto_now = True) #추가
    objects = UserManager()

    USERNAME_FIELD = 'user_ID'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
   # class Meta:
       # db_table = "Account"
#db_table = 'Account' # 테이블명을 user로 설정 -> Account로 변경함