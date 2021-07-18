from .models import DayPlans, Letters, Profile
from django.forms import ModelForm, DateInput, Textarea, CharField, EmailField, PasswordInput, BooleanField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class DayPlansForm(ModelForm):
    class Meta:
        model = DayPlans
        fields = ['date', 'plan']

        widgets = {
            'plan': Textarea(attrs={
                'placeholder': 'Вынести мусор'
            }), 
            'date': DateInput(attrs={
                # 'type': 'date',
                'placeholder': 'Дата'
            })
        }

class Change_passwordForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']

    widgets = {
        'password': PasswordInput(attrs={
            'id': 'password-input'
        })
    }

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    widgets = {
            'password': PasswordInput(attrs={
                'id': 'password-input'
            })
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
        widgets = {
            'password': PasswordInput(attrs={
                'id': 'password-input'
            })
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
            
        self.fields["username"] = CharField(
            max_length=40,
            min_length=5)

        validator_user = RegexValidator(r'^[a-zA-Z0-9]*$')
        validator_password = RegexValidator(r'^[a-zA-Z0-9-=$!|?*+./]*$')
        self.fields['username'].validators = [validator_user]
        self.fields['password'].validators = [validator_password]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# class AnotherUserFieldsForm(forms.ModelForm):
#     class Meta:
#         model = AnotherUserFields
#         fields = ['theme']
#         widgets = {
#             'theme': BooleanField(attrs={'class': 'date'}),
#         }

class LettersForm(ModelForm):
    class Meta:
        model = Letters
        fields = ['letter']

        widgets = {
            'letter': Textarea(attrs={
                'class': 'contact_textaria'
            })
        }