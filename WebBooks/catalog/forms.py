from django import forms
from datetime import date
from .models import Author, Book


class Form_add_author(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фaмилия автора')
    date_of_birth = forms.DateField(
        label = 'Дата рождения',
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': date})
    )
    about = forms.CharField(label='Cвeдeния об авторе',
                            widget=forms.Textarea)
    photo = forms.ImageField(label = 'Фото автора')

class Form_edit_author(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['summary',]
        labels = {'summary': ('Аннотация'),}
        help_text = {'summary': ('Не более 1000 символов'), }
