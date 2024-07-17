from django import forms
from medicioapp.models import Appoint, ImageModel

class AppointForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields =['name','email','phone','date','doctor','message','department']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']