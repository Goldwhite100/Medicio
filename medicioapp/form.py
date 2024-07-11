from django import forms
from medicioapp.models import Appoint

class AppointForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields =['name','email','phone','date','doctor','message','department']