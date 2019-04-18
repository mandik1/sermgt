from django import forms
from .models import Service, Appointement



class AddServiceForm(forms.ModelForm):
    class Meta:
            
        model = Service
        fields = '__all__'

class AppointementForm(forms.ModelForm):
    class Meta:
            
        model = Appointement
        exclude = ('is_active',)