from django import forms

from mail_sender.models import Settings, MailingList


class MixinFormStile:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(MixinFormStile, forms.ModelForm):
    class Meta:
        model = MailingList
        fields = ('name', 'settings', 'settings', 'clients')
