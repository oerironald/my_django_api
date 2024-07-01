from django import forms

class CountryForm(forms.Form):
    country = forms.CharField(label='Country', max_length=100)




class SymbolForm(forms.Form):
    SYMBOL_CHOICES = [
        ('AAPL', 'Apple Inc.'),
        ('MSFT', 'Microsoft Corporation'),
        ('GOOGL', 'Alphabet Inc. (Google)'),
        ('AMZN', 'Amazon.com, Inc.'),
        ('TSLA', 'Tesla, Inc.'),
        ('META', 'Meta Platforms, Inc. (Facebook)'),
    ]
    symbol = forms.ChoiceField(choices=SYMBOL_CHOICES, label='Stock Symbol')


class CountrySelectForm(forms.Form):
    country = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].choices = [('all', 'All Countries')] + [(country, country) for country in self.get_countries()]

    def get_countries(self):
        import requests
        response = requests.get('https://disease.sh/v3/covid-19/countries')
        countries = [country['country'] for country in response.json()]
        return sorted(countries)