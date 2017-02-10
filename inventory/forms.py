__author__ = 'praveen'

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from inventory.models import Item
from inventory.models import Comment

class MyRegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)

    class Meta:
        model= User
        fields= ('username', 'first_name' ,'last_name' , 'email', 'password1', 'password2')

    def save(self, commit=True):
        user= super(MyRegistrationForm, self).save(commit= False)
        user.email= self.cleaned_data['email']
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.is_staff= True

        if commit:
            user.save()

        return user

class ItemForm(forms.ModelForm):

    class Meta:
        model= Item
        fields= ('title', 'description', 'pub_date')


class CommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields= ('name', 'body')


class EditProfileForm(forms.ModelForm):
    email= forms.EmailField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)

    class Meta:
        model = User
        fields= ('username', 'first_name', 'last_name', 'email')

    # def __init__(self, *args, **kwargs):
    #     current_user = kwargs.pop('current_user')
    #     super(EditProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['employer'] = current_user