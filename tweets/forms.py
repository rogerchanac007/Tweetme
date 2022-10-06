from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Your message"}))
    class Meta:
        model = Tweet
        fields = [
            #"user",
            "content",
        ]
    
    # def clean_content(self, **args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == "abc":
    #         raise forms.ValidationError("No puede ser abc")
    #     return content