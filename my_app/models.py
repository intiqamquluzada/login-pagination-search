from django.db import models
from services.extract import extract_google_maps_url_from_iframe

SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok")
)


class Our_Services(models.Model):
    name = models.CharField(max_length=255, verbose_name='servis adi', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'servis'
        verbose_name_plural = 'servisler'


class Portfolio(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class About(models.Model):
    name = models.CharField(max_length=255, verbose_name='basliq')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'basliq'
        verbose_name_plural = 'basliqlar'


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='ad')
    mail = models.CharField(max_length=255, verbose_name='mail')
    tel = models.IntegerField(verbose_name='telefon nomresi')
    contact_service = models.CharField(max_length=255, null=True, blank=True)
    mesage = models.CharField(max_length=255, verbose_name='mesage', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'ad'
        verbose_name_plural = 'adlar'


class MAINDETAILS(models.Model):
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=255, verbose_name='telefon nomresi')
    location = models.CharField(max_length=255, verbose_name='mekan')
    logo = models.ImageField(upload_to='media/', null=True, blank=True)
    map_url = models.TextField(verbose_name='xerite', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('email',)
        verbose_name = 'esas detal'
        verbose_name_plural = 'esas detallar'

    def save(self, *args, **kwargs):
        extracted_url = extract_google_maps_url_from_iframe(self.map_url)
        if extracted_url:
            self.map_url = extracted_url
        super(MAINDETAILS, self).save(*args, **kwargs)


class SocialMedia(models.Model):
    social_name = models.CharField(max_length=255, verbose_name="Sosial media hesabi", choices=SOCIAL_CHOICES)
    social_link = models.TextField(verbose_name="Sosial media linki")

    def __str__(self):
        return self.social_name

    class Meta:
        ordering = ("social_name",)
        verbose_name = "Sosial media hesabi"
        verbose_name_plural = "Sosial media hesablari"
