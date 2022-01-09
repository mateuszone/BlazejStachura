from django import forms

from www.models import Contact


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class ContactForm(forms.ModelForm):
    # name = forms.CharField(label='imię', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    # email = forms.EmailField(label='email')
    # phone = forms.IntegerField()
    # place_of_performance = forms.CharField()
    # date_of_performance = forms.DateTimeField()
    # message = forms.TextInput()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'place_of_performance', 'date_of_performance', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Imię'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Adres email'}),
            'phone': forms.NumberInput(
                attrs={'placeholder': 'Numer telefonu'}),
            'place_of_performance': forms.TextInput(
                attrs={'placeholder': 'Miejsce występu'}),
            'date_of_performance': DateInput(),
            'message': forms.Textarea(
                attrs={'placeholder': 'Wiadomość'}),
        }
