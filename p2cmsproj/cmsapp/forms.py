from django import forms
from .models import DeptModel
from .models import StuModel


class DeptForm(forms.ModelForm):
	class Meta:
		model = DeptModel
		fields = "__all__"


class StuForm(forms.ModelForm):
	class Meta:
		model = StuModel
		fields = "__all__"