# coding=utf-8
from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a')
    b = forms.IntegerField(label='коэффициент b')
    c = forms.IntegerField(label='коэффициент c')

    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом не может быть равен нулю")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data