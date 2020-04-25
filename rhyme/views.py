from django.views.generic import TemplateView
from rhyme.settings import STATIC_DIR
from .utils import find_chinese
import functools
import json
from pypinyin import pinyin, Style


class IndexView(TemplateView):
    template_name = "index.html"


class SearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # dealing input
        words = find_chinese(query)
        if not words:
            context['results'] = []
        else:
            py = pinyin(words, style=Style.FINALS, errors='ignore')
            key = functools.reduce(lambda a, b : a + b, py)
            key = '-'.join(key)
            # read data
            with open(STATIC_DIR + '/data/result.json', 'r') as f:
                rhyme_dict = json.load(f)
            try:
                context['results'] = rhyme_dict[key]
            except KeyError:
                context['results'] = []
        return context
