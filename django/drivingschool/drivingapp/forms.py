from django import forms

class PlanningForm(forms.Form):
	date = forms.CharField(label="date", max_length=100)
	lieu = forms.CharField(label="lieu", max_length=100)