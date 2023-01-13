from django import forms
from .models import Post
# creating a form
class BlogForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Post
        fields = [
            "title", "author", "body",  "status"
        ]
        
        
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
         
            "author": forms.TextInput(attrs={'class': 'form-control', 'required': 'false',  'value': '', 'id': 'users_id', 'type': 'hidden'}),

            'body': forms.Textarea(attrs={'class': 'form-control', 'required': 'false'}),
            
            
            'status': forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
        }
        # fields = "__all__"