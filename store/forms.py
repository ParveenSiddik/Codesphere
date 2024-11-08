from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from store.models import UserProfile,Project

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","password1","password2"]

        widgets={
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.TextInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"}),
        }

class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"})) 

         

class UserProfileForm(forms.ModelForm):

    class Meta:

        model=UserProfile

        fields=["bio","profile_picture","phone"]

class ProjectForm(forms.ModelForm):

    class Meta:

        model=Project        

        fields=["title","description","preview_image","price",
        "files","tag_objects","thumbnail"]

class PasswordResetForm(forms.Form):

    username=forms.CharField()

    email=forms.CharField()

    password1=forms.CharField()

    password2=forms.CharField()          
