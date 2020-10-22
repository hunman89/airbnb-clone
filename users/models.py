from django.contrib.auth.models import AbstractUser
from django.db import models

# 다른 객체는 Model 객체를 상속 database와 커뮤니케이션 한다.
# user는 이미 존재하는 auth.models를 불러와 상속한다.


class User(AbstractUser):

    """ Custom User Model """

    # Model field
    # db colunm = django name

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "english"),
        (LANGUAGE_KOREAN, "korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)