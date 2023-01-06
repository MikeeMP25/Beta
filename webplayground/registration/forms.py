from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Este metodo te permitira validar si el correo existe en la base de datos si es el caso no te premitira
    # registrar nuevamente el correo haciendo el atributo unico e irrepetible
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya esta registrado en la plataforma, prueba con otro correo.")
        return email
