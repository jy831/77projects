from django import forms
from pickever.models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist']