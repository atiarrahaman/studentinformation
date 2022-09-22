from django  import forms
from django.forms import fields, widgets
from .models import *

class edit_form(forms.ModelForm):
    
    class Meta:
        model = Students_info
        fields = ("name","roll","address","phone","student_class","distic")
        widgets={

              'name':forms.TextInput(attrs={'class':'form-control'}),
              'roll':forms.TextInput(attrs={'class':'form-control'}),
              'address':forms.TextInput(attrs={'class':'form-control'}),
              'phone':forms.TextInput(attrs={'class':'form-control'}),
              

        }

class input_form(forms.ModelForm):
    class Meta:
        model=Students_info
        fields= ('name','roll','address','phone','student_class','distic')
        widgets={

              'name':forms.TextInput(attrs={'class':'form-control'}),
              'roll':forms.TextInput(attrs={'class':'form-control'}),
              'address':forms.TextInput(attrs={'class':'form-control'}),
              'phone':forms.TextInput(attrs={'class':'form-control'}),
              

        }
