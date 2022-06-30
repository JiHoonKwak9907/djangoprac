from dataclasses import fields
from django import forms
from .models import Blog, Comment #model형식의 입력을 받기 위함임


class BlogForm(forms.Form):
  #내가 입력받고자 하는 값들
  title = forms.CharField()
  body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = '__all__' #이러면 전부 입력받는 것임
    # fields = ['title', 'body'] #이러면 일부만 골라서 입력받는 것임

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']