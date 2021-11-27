from django import forms
from django.core.exceptions import ValidationError
from app1.models import deptname

class homeforms(forms.ModelForm):
    class Meta:
        model = deptname
        fields='__all__'
    def clean(self):
        un= self.cleaned_data['facultyname']
        if not(3<=len(un)<=20): 
            raise forms.ValidationError("plz enter the min 3 characters and max 10 characters")
        dt= self.cleaned_data['doj']
        res=str(dt)[0:4]
        if not(1975<=int(res)<=2021): 
            raise forms.ValidationError("plz enter the min 1975 year to max 2021 year")

class choicedisplay(forms.Form):
    li=[['ALL','ALL'],['IT','It'],['ELECTRICAL','Electrical'],['MECHANICAL','Mechanical'],['COMMON','COMMON']]
    choicedept= forms.ChoiceField(choices=li)