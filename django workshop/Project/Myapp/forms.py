from django import forms
from django.forms import ModelForm
from Myapp.models import Register

class Reg(forms.ModelForm):
	class Meta:
		model = Register
		fields =['name','mobile_no','age','gender','branch']
		widgets ={
			'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
			'mobile_no':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile number'}),
			'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
			'gender':forms.RadioSelect(attrs={'type':'radio','placeholder':'Select gender'}),
			'branch':forms.Select(attrs={'class':'form-control'}),
		}

