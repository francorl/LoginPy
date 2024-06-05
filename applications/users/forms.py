from django import forms
from django.contrib.auth import authenticate
from .models import User



class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password'
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'lastname', 'gender')


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match")


class LoginForm(forms.Form):
        username = forms.CharField(
            label='username',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'username'
                }
            )
        )
        password = forms.CharField(
            label='contraseña',
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Contraseña'
                }
            )
        )

        def clean(self):
            cleaned_data = super(LoginForm, self).clean()
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Incorrect username or password")
            return self.cleaned_data

class UpdatePasswordForm(forms.Form):
        password1 = forms.CharField(
            label='contraseña',
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Contraseña Antigua'
                }
            )
        )
        password2 = forms.CharField(
            label='contraseña',
            required=True,
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': 'Contraseña Nueva'
                }
            )
        )
#DWRM38EUUGHYSM4JWEFH2TCA
class VerificationForm(forms.Form):
        codregistro  = forms.CharField(required=True)


        def __init__(self, pk, *args, **kwargs):
            self.id_user = pk
            super(VerificationForm, self).__init__(*args, **kwargs)

        def clean_codregistro(self):
            codigo = self.cleaned_data['codregistro']

            if len(codigo) == 6:
                activo = User.objects.codregistro(
                    self.id_user,
                    codigo)
                if not activo:
                    raise forms.ValidationError('Codigo no activo')
            else:
                raise forms.ValidationError("Codigo incorrecto")

