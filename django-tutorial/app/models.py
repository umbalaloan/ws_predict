from django.db import models
# Create your models here.
class UploadFileModel(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')



