from django import forms
from django.contrib.auth.models import User
from .models import Author
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# class AuthorForm(forms.ModelForm):
#     class Meta: 
#         model = Author
#         fields = '__all__'
#         # fields = ['name', 'bio']
#         # exclude = ['bio']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    # organizer_or_not = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'not_required'}))


    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

        # def save(self,commit=True):
        #     our_user = super().save(commit=False)
        #     if commit == True:
        #         print("User_name")
        #         our_user.save()
        #         organizer_or_not = self.cleaned_data.get('organizer_or_not')

        #         Author.objects.create(
        #             user = our_user,
        #             organizer_or_not = organizer_or_not
        #         )
        #     else:
        #         print("name:",our_user.first_name)
        #     return our_user




class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']