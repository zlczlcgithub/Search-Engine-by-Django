from django.db.models import Q
from django.shortcuts import render
from .forms import SearchFormSet
from .models import Sentence


def index(request):
    search_list = None
    formset = SearchFormSet(request.POST or None)
    if request.method == 'POST':
        queries = []
        if formset.is_valid():
            # OR search -> Q  
            for form in formset:
                # {super_cat: 'ADJECTIVES', sub_cat: 'superlatives'} → Q(super_cat='ADJECTIVES', sub_cat='superlatives')
                q_kwargs = {}
                sentence = form.cleaned_data.get('sentence')
                if sentence:
                    q_kwargs['sentence'] = sentence
                super_cat = form.cleaned_data.get('super_cat')
                if super_cat:
                    q_kwargs['super_cat'] = super_cat
                sub_cat = form.cleaned_data.get('sub_cat')
                if sub_cat:
                    q_kwargs['sub_cat'] = sub_cat

                if q_kwargs:
                    q = Q(**q_kwargs)
                    queries.append(q)

        if queries:
            # filter(Q(...) | Q(...) | Q(...))
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            search_list = Sentence.objects.all()
            search_list = search_list.filter(base_query)
    context = {
        'search_list': search_list,
        'formset': formset,
    }
    return render(request, 'search.html', context)
