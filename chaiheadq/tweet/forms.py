from django import forms
from .models import Tweet

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