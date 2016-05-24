from django import forms


DISTANCES = (('10', 10),
             ('20', 20),
             ('30', 30),
             ('50', 50),
             ('75', 75),
             ('100', 100))


class AllForm(forms.Form):
    zipcode = forms.CharField(max_length=5, required=True,
                              label='Starting Zipcode',
                              widget=forms.TextInput(
                                    attrs={'class': 'zip_form'}))
    distance = forms.ChoiceField(choices=DISTANCES,
                                 required=True,
                                 label='Distance (Miles)',
                                 widget=forms.Select(
                                       attrs={'class': 'distance_form'}))
    produce = forms.CharField(label='Produce',
                              required=False,
                              widget=forms.Textarea(
                                    attrs={'class': 'produce_form'}))


<<<<<<< HEAD
class ZipCodeForm(forms.Form):
    zipcode = forms.CharField(max_length=5, required=True,
                              label='Starting Zipcode',
                              widget=forms.TextInput(
                                    attrs={'class': 'zip_form'}))


class DistanceForm(forms.Form):
    distance = forms.ChoiceField(choices=DISTANCES,
                                 required=True,
                                 label='Distance (Miles)',
                                 widget=forms.Select(
                                       attrs={'class': 'distance_form'}))


class ProduceForm(forms.Form):
        produce = forms.CharField(label='Produce',
                                  required=False,
                                  widget=forms.Textarea(
                                        attrs={'class': 'produce_form'}))
=======
class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
>>>>>>> d47e8bf3f253445201a5c065462c7000c8ff604c
