from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'number_of_people', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_time(self):
        time = self.cleaned_data['time']

        if time.hour < 8 or time.hour >= 18:
            raise forms.ValidationError("Booking time should be between 8 am and 6 pm.")

        return time