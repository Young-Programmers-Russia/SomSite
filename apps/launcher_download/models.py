from django.db import models


class Launcher(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    file = models.FileField(upload_to='launchers/')

    def __str__(self):
        return str(self.file)