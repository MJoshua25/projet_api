from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mois(models.Model):
    """Model definition for Mois."""

    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(upload_to='mois')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Mois."""

        verbose_name = 'Mois'
        verbose_name_plural = 'Moiss'

    def __str__(self):
        """Unicode representation of Mois."""
        return self.titre


class Module(models.Model):
    """Model definition for Module."""

    # TODO: Define fields here
    mois = models.ForeignKey('Mois', related_name='Modules', on_delete=models.CASCADE)
    langage = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Module')
    description = models.TextField()
    prix = models.IntegerField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Module."""

        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        """Unicode representation of Module."""
        return self.langage


class Chapitre(models.Model):
    """Model definition for Chapitre."""

    # TODO: Define fields here
    module = models.ForeignKey('Module', related_name='chapitres', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    description = models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Chapitre."""

        verbose_name = 'Chapitre'
        verbose_name_plural = 'Chapitres'

    def __str__(self):
        """Unicode representation of Chapitre."""
        return self.titre

class Cour(models.Model):
    """Model definition for Cour."""

    # TODO: Define fields here
    chapitre = models.ForeignKey('Chapitre', related_name='cours', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    video = models.FileField(upload_to='cour', max_length=100)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for Cour."""

        verbose_name = 'Cour'
        verbose_name_plural = 'Cours'

    def __str__(self):
        """Unicode representation of Cour."""
        return self.titre


class User_Course(models.Model):
    """Model definition for User_Course."""

    # TODO: Define fields here
    module = models.ForeignKey('Module', related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='modules', on_delete=models.CASCADE)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        """Meta definition for User_Course."""

        verbose_name = 'User_Course'
        verbose_name_plural = 'User_Courses'

    def __str__(self):
        """Unicode representation of User_Course."""
        return self.module

