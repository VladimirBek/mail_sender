from blog.models import BlogPost
from django import forms


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.user
        if commit:
            instance.save()
        return instance