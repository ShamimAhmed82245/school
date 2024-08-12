from django import forms
from .models import Teacher

class TeachersForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        # fields = ['name','email','phone_number','bio']
        fields = "__all__"
        exclude = ['email']
        labels={
            'name':"Your Name",
            'email':"Your Email",
            'phone_number':"Contact Number",
            'bio':"Yours Details"
        }
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'phone_number':forms.NumberInput(attrs={'class':"form-control"}),
            'bio':forms.Textarea(attrs={'class':"form-control"})

        }

        help_texts={
            'email':"We only accept gmail."
        }

        error_messages={
            'name':{
                'required':'Name field is required'
            }
        }










    # name = forms.CharField(min_length=5,label='Your Name',label_suffix="",
    #                        error_messages={'required':"Your name field cannot be empty", 'min_length':"The minimum length of name is 5"}
    #                        ,widget=forms.TextInput(attrs={'class':"form-control"}))
    # email = forms.EmailField(required=False,label='Your Email',label_suffix="",widget=forms.EmailInput(attrs={'class':"form-control"}))
    # phone_number = forms.IntegerField(label='Contact Number',label_suffix="",widget=forms.NumberInput(attrs={'class':"form-control"}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"bio",'rows':20,'cols':60,'class':"form-control"}))