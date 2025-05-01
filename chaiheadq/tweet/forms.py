from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

    # def clean_text(self):
    #     text = self.cleaned_data.get('text')
    #     if len(text) > 240:
    #         raise forms.ValidationError("Text exceeds 240 characters limit.")
    #     return text

    # def clean_photo(self):
    #     photo = self.cleaned_data.get('photo')
    #     if photo and photo.size > 5 * 1024 * 1024:  # 5 MB limit
    #         raise forms.ValidationError("Photo size exceeds 5 MB limit.")
    #     return photo
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') # Using tuple instead of array because we are using builtin form here