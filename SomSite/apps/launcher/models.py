from django.db import models


class Launcher(models.Model):
    OS_VERSIONS = [
        ("LINUX", "Linux"),
        ("WINDOWS", "Windows"),
        ("MAC", "Mac"),
    ]
    storage = 'launchers/'
    version = models.CharField(
        max_length=50,
    )
    os = models.CharField(
        max_length=7, 
        choices=OS_VERSIONS,
    )
    file = models.FileField(
        upload_to=storage,
    )
    archive = models.FileField(
        upload_to=storage,
    )

    def __str__(self):
        return str(self.file.name.strip(self.storage))
