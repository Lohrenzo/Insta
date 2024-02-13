from django import forms
from .models import Post, Category, Comment

# choices =  [('sports','sports'), ('music','music'), ('comedy','comedy')]
choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("pic", "caption", "author", "category")

        widgets = {
            "pic": forms.FileInput(attrs={"class": "form-control"}),
            "caption": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Drop a catchy Caption",
                }
            ),
            "author": forms.TextInput(
                attrs={"class": "form-control", "id": "postauthor", "type": "hidden"}
            ),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("pic", "caption", "category")

        widgets = {
            "pic": forms.FileInput(attrs={"class": "form-control"}),
            "caption": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Drop a catchy Caption",
                }
            ),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("username", "body")

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "id": "commentauthor", "type": "hidden"}
            ),
            "body": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write a Comment",
                }
            ),
        }
