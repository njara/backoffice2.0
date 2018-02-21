from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings


# Create your models here.


def get_image_path_company(instance, filename):
    return os.path.join('company_icon', str(instance.id), filename)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(BaseModel):
    ACCOUNT_STATUS = (
        (0, 'Creada'),
        (1, 'Activada'),
        (2, 'Bloqueada'),
    )
    token = models.CharField(max_length=16)
    status = models.IntegerField(null=True, default=0, choices=ACCOUNT_STATUS)

    def get_status_name(self):
        if self.status is not None:
            return self.ACCOUNT_STATUS[self.status][1]
        else:
            return ''

    def is_enabled(self):
        return self.status == 1

    def __str__(self):
        return 'Cuenta'

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'


class UserProfile(AbstractUser, BaseModel):
    last_seen = models.DateTimeField(null=True, blank=True)
    app_installed = models.BooleanField(default=False)
    account = models.ForeignKey(Account, related_name='user_account', on_delete=models.PROTECT, null=True, )

    def is_enabled(self):
        try:
            return self.account.is_enabled()
        except AttributeError:
            return False

    def get_user_str(self):
        return self.account.get_status_name()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de usuario'

    REQUIRED_FIELDS = ["email"]


class Company(BaseModel):
    name = models.CharField('Nombre', max_length=40)
    identifier = models.CharField('Identificador', max_length=16)
    icon = models.ImageField('Imagen/Logo', upload_to=get_image_path_company, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.identifier, self.name)

    class Meta:
        verbose_name = 'Comercio'
        verbose_name_plural = 'Comercios'


class ExpirationDateCard(models.Model):
    YEAR_ENABLED = (
        (0, '2018'),
        (1, '2019'),
        (2, '2020'),
        (3, '2021'),
        (4, '2022'),
        (5, '2023'),
        (6, '2024'),

    )
    MONTH_ENABLED = (
        (1, '01'),
        (2, '02'),
        (3, '03'),
        (4, '04'),
        (5, '05'),
        (6, '06'),
        (7, '07'),
        (8, '08'),
        (9, '09'),
        (10, '10'),
        (11, '11'),
        (12, '12'),

    )
    month = models.IntegerField(null=False, default=0, choices=YEAR_ENABLED)
    year = models.IntegerField(null=False, default=0, choices=MONTH_ENABLED)

    def get_expiration_date(self):
        if self.month is not None and self.year is not None:
            return '{} / {}'.format(self.MONTH_ENABLED[self.month][1], self.YEAR_ENABLED[self.year][1])
        else:
            return ''


class Emisor(BaseModel):
    name = models.CharField('nombre', max_length=40)
    identifier = models.CharField('Identificador', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Emisor'
        verbose_name_plural = 'Emisores'


class Card(BaseModel):
    CARD_TYPES = (
        (0, 'MasterCard'),
        (1, 'Visa'),
    )
    type = models.IntegerField(null=False, default=0, choices=CARD_TYPES)
    alias = models.CharField('Alias', max_length=40)
    expiration_date = models.ForeignKey(ExpirationDateCard, related_name='expiration_date_card',
                                        on_delete=models.CASCADE, )
    emisor = models.ForeignKey(Emisor, related_name='card_emisor', on_delete=models.CASCADE, )
    number = models.CharField('Nº tarjeta', max_length=16)
    cvv = models.CharField('Código de Verificación', max_length=4)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'


class Device(BaseModel):
    name = models.CharField('Nombre', max_length=40)
    identifier = models.CharField('Identificador', max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
