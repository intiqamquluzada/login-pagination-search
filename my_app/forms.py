from django import forms
from my_app.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "mail", "tel", "mesage", "contact_service",)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        self.fields['name'].widget.attrs.update({"placeholder": "Adınız"})
        self.fields['mail'].widget.attrs.update({"placeholder": "E-poçt ünvanı"})
        self.fields['tel'].widget.attrs.update({"placeholder": "Əlaqə nömrəsi"})
        self.fields['mesage'].widget.attrs.update({"placeholder": "Mesaj", "class": "message-box form-control"})
