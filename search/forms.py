from django import forms
from .models import Sentence


class SearchForm(forms.Form):
    sentence = forms.CharField(label='sentence')
    super_cat = forms.CharField(label='super_cat', required=False)
    sub_cat = forms.CharField(label='sub_cat', required=False)


SearchFormSet = forms.formset_factory(SearchForm, extra=3)
