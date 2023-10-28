from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from backend.models import CustomUser, Organization, Jedzenie, Przedmiot, Image, Usluga, Event
from .validator import file_size

class FormUserRegistration(UserCreationForm):
    telefon = forms.CharField(max_length=12)
    email = forms.EmailField()
    # adres_zamieszkania = forms.CharField()
    # data_urodzenia = forms.DateField()
    # avatar = forms.ImageField()
    # rola = forms.CharField()


    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'telefon', 'email', 'password1', 'password2', 'adres_zamieszkania', 'data_urodzenia', 'avatar', 'rola']
        # help_texts = {
        #     'username': None,
        #     'password2': None,
        # }

    def save(self, commit=True):
        user = super(FormUserRegistration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.telefon = self.cleaned_data['telefon']
        user.adres_zamieszkania = self.cleaned_data['adres_zamieszkania']
        user.data_urodzenia = self.cleaned_data['data_urodzenia']
        user.avatar = self.cleaned_data['avatar']
        user.rola = self.cleaned_data['rola']
        if commit:
            user.save()
        return user
    
class FormOrganizationCreate(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['nazwa', 'opis', 'logo']


TITLE_CHOICES = [
    ('Sportowe', 'Sportowe'),
    ('Kulturowe', 'Kulturowe'),
    ('Rozrywkowe', 'Rozrywkowe'),
]


class FormEventCreate(forms.Form):
    # image = MultipleFileField(label='Zdjęcia dodatkowe', required=False, validators=[file_size], widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_date', 'event_location', 'type_of_event', 'main_image', 'link_do_miejsca_wydarzenia']

    # event_name = forms.CharField(max_length=100, required=False)
    # event_description = forms.CharField(max_length=500, required=False)
    # event_date = forms.DateTimeField()
    # event_location = forms.CharField(max_length=100, required=False)
    # type_of_event = forms.CharField(max_length=30, widget=forms.Select(choices = TITLE_CHOICES),)
    # main_image = forms.ImageField()
    # link_do_miejsca_wydarzenia =  forms.URLField(max_length = 200, required=False)
    # x_miejsca = forms.FloatField()
    # y_miejsca = forms.FloatField()
    # image = forms.MultipleFileField(label='Zdjęcia dodatkowe', required=False, validators=[file_size], widget=forms.ClearableFileInput(attrs={'multiple': True}))

    # title = forms.CharField(label='Nazwa wydarzenia', max_length=100, widget=forms.TextInput(attrs={'class':'task_window', 'placeholder':'Zawody sportowe'}))
    # description = forms.CharField(label='Opis', max_length=300, widget=forms.Textarea(attrs={'class':'task_window', 'placeholder':'Otwarty turniej piłkarski', 'rows' : 5}))
    # main_image = forms.ImageField(label='Główne zdjęcie', required=False)
    # start_time = forms.DateField(label='Data rozpoczęcia', widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    # start_time_time = forms.TimeField(label="", widget=TimePickerInput)
    # deadline = forms.DateField(label='Przewidywana data zakończenia', widget=NumberInput(attrs={'type': 'date', 'class':'task_date'}))
    # deadline_time = forms.TimeField(label="Przewidywana odzina zakończenia", widget=TimePickerInput)
    # type_of_event = forms.CharField(label='Wybierz rodzaj wydarzenia',
    #     widget=forms.Select(choices = TITLE_CHOICES, attrs={'class':'task_window'}),
    #     required=True
    # )
    # link_do_miejsca_wydarzenia = forms.URLField(required=False, label='Link', max_length = 200, widget=forms.URLInput(attrs={'class':'task_window'}))
    # x = forms.FloatField(label='Naciśnij na mapę aby wybrać współrzędne geograficzne', required=True, widget=forms.NumberInput(attrs={'id': 'x', 'step': "0.0000000001"}))
    # y = forms.FloatField(label='', required=True, widget=forms.NumberInput(attrs={'id': 'y', 'step': "0.0000000001"}))
    # image = forms.FileField(label='Zdjęcia dodatkowe', required=False, validators=[file_size], widget=forms.ClearableFileInput(attrs={'multiple': True}))

class FormJedzenie(forms.Form):
    class Meta:
        model = Jedzenie
        fields = ['food_name', 'food_description', 'food_image']


class FormPrzedmiot(forms.Form):
    class Meta:
        model = Przedmiot
        fields = ['item_name', 'item_description', 'item_image']


class FormUsluga(forms.Form):
    class Meta:
        model = Usluga
        fields = ['service_name', 'service_description', 'service_price', 'service_image']


      