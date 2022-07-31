from django import forms
from pickever.models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '제목',
            'artist': '가수',
        }