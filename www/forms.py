from django import forms

from www.models import Contact, Event


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class ContactForm(forms.ModelForm):

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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)
