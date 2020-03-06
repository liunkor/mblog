from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    website = forms.CharField(
        label='website',
        max_length=100,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width:60%;'}
        )
    )

    content = forms.CharField(
        label='comment content',
        max_length=2000,
        widget=forms.widgets.Textarea(
            attrs={'rows': 6, 'cols': 60, 'class': 'form-control'}
        )
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('The length of comment is toot short!')
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']
