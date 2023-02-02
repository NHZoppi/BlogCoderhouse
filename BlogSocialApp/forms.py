from django import forms
from .models import Post, Avatar
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    content = RichTextField(blank= True, null = True)
    image = forms.FileField(required= True)
    title = forms.CharField()
    description = forms.CharField()
    class Meta:
        model = Post
        fields = ['title','description','content', 'image']
    enctype = "multipart/form-data"


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput)



class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']

