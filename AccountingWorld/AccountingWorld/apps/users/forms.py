from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Please enter a valid email address.', required=True)

    class Meta:
        model = get_user_model()  # retrieve the custom user model specified in the 'AUTH_USRE_MODEL'
        fields = ('username', 'email', 'password1', 'password2')

    # By default, UserCreationForm validates the uniqueness of the username and the passwords to make sure they match
    # However, it does not include validation for the uniqueness of  the email field, To enforce that the email field is
    # unique and not used by any other user in the database, you need to add custom validation to the form
    # you can achieve this by overriding the 'clean_email' method to check if the provided email already exists in
    # the database

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model()  # Get the custom user model class
        if email and user.objects.filter(email=email).exists():
            raise forms.ValidationError('The email already is already in use. Please use a different email.')
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = get_user_model()  # get the custom user model class
        if not user.objects.filter(email=email).exists():
            raise forms.ValidationError("The email is not registered yet. Please register")
        elif user.objects.filter(email=email, is_active=False).first():
            raise forms.ValidationError("The email is registered but not activated. Please check your mail and activate")
        else:
            pass
        return email