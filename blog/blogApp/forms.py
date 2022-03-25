from django import forms
from .models import Post, Category, Comment

# Query for all category objects
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for choice in choices:
    choice_list.append(choice) 

# Form for creating a new blog post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'article_hook', 'header_image', 'image_alt')

        widgets = {
            'title' : forms.TextInput(attrs={}),
            'title_tag' : forms.TextInput(attrs={}),
            'author' : forms.TextInput(attrs={'id' : 'authorBox', 'value' : '', 'type' : 'hidden'}),
            'category' : forms.Select(choices=choice_list),
            'article_hook' : forms.Textarea(),
            'body' : forms.Textarea(attrs={}),
            'image_alt' : forms.TextInput(attrs={}),
        }

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for fields in self.visible_fields():
                fields.field.widget.attrs["class"] = 'post-forms'

# Form for editing a blog post
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'header_image', 'image_alt')

        widgets = {
            'title' : forms.TextInput(attrs={}),
            'title_tag' : forms.TextInput(attrs={}),
            'category' : forms.Select(choices=choice_list, attrs={}),
            'article_hook' : forms.Textarea(),
            'body' : forms.Textarea(attrs={}),
            'image_alt' : forms.TextInput(attrs={}),
        }

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for fields in self.visible_fields():
                fields.field.widget.attrs["class"] = 'post-forms'


# Form for comments
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Comment
        fields =['body']

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for fields in self.visible_fields():
                fields.field.widget.attrs["class"] = 'post-forms'