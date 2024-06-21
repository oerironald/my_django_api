from django import forms

class PatientForm(forms.Form):
    given_name = forms.CharField(label='Given Name', max_length=100)
    family_name = forms.CharField(label='Family Name', max_length=100)
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female')])
    birthdate = forms.DateField(label='Birthdate', widget=forms.DateInput(attrs={'type': 'date'}))

class PatientSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Query', required=False)