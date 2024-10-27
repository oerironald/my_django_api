from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField


GENDER_CHOICES = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Other", "Other"),
)

IDENTITY_TYPE_CHOICES = (
    ("National Identification Number", "National Identification Number"),
    ("Driver's License", "Driver's License"),
    ("International Passport", "International Passport"),
)

def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f"user_{instance.user.id}/{filename}"

class User(AbstractUser):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=108, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Other")
    otp = models.CharField(max_length=100, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet="abcdefghijklmnopqrstunoyz123")
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=190, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="other")
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    
    identity_type = models.CharField(max_length=200, choices=IDENTITY_TYPE_CHOICES, null=True, blank=True)
    identity_image = models.FileField(upload_to=user_directory_path, default="id.jpg", null=True, blank=True)
    
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.full_name:
            return f"{self.user.username}"
        

# Signal to create or update the Profile when the User instance is saved
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.Profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)