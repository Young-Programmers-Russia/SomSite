from django import forms


class MultipleModsInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleModsFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleModsInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ModsFileFieldForm(forms.Form):
    file_field = MultipleModsFileField()
