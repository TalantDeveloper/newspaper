from django.db import models


class Magazine(models.Model):
    """
    Jurnal models
    """
    title = models.CharField(max_length=255, verbose_name="Nomi")
    content = models.TextField(verbose_name="Tafsilot")
    image = models.ImageField(upload_to="image/", verbose_name="Rasm")
    file = models.FileField(upload_to="file/", verbose_name="Jurnal")

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
