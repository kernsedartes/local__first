from django import forms

class DealForm(forms.Form):
    title = forms.CharField(label='Название сделки', max_length=255)
    stage_id = forms.CharField(label='Стадия', max_length=50)
    currency = forms.ChoiceField(
        label='Валюта',
        choices=[
            ('RUB', 'Рубли'),
            ('USD', 'Доллары'),
            ('EUR', 'Евро'),
        ]
    )
    price = forms.DecimalField(label='Сумма сделки', max_digits=10, decimal_places=2)
    begindate = forms.DateField(label='Дата начала сделки', widget=forms.DateInput(attrs={'type': 'date'}))
    closedate = forms.DateField(label='Дата конца сделки', widget=forms.DateInput(attrs={'type': 'date'}))
    custom_field = forms.CharField(label='Место встречи', max_length=255)
