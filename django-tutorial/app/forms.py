from django.forms import forms
from app.models import UploadFileModel
class UploadForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    class Meta:
        model = UploadFileModel()