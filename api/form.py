from django import forms
from .models import Pendaftaran


# creating a form
class PendaftaranForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Pendaftaran

        # specify fields to be used
        fields = [
            'nama', 'npm', 'email', 'motivasi', 'menjadi_pengurus',
            'minat', 'hari', 'bahasa', 'harapan',
        ]
