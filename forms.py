from django import forms
from .models import profile
from django_countries.widgets import CountrySelectWidget

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('job', 'description', 'location')
        exclude = ('name', 'user')

        widgets={
            "job":forms.TextInput(attrs={'placeholder':'Quel est votre travail...'}),
            "description":forms.Textarea(attrs={'placeholder':'Résumé votre quotidien...'}),
            "location": CountrySelectWidget()
        }
