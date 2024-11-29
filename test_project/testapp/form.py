from django import forms
from testapp.models import Student 

# ModelForm is used to generate HTML form automatically in Django
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student        
        fields=('rno','marks')