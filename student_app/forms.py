from email.policy import default
from stat import FILE_ATTRIBUTE_ARCHIVE

from django import forms
from django.db.models import CharField


class ProgramInfoForm(forms.Form):
    program_name=forms.CharField(max_length=20)
    student_count=forms.IntegerField()
    selectedIds=forms.CharField(max_length=255,required=True)
    program_message=forms.CharField(max_length=210)
    program_document=forms.FileField(required=False)




