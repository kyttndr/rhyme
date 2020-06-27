from django.views.generic import TemplateView
from rhyme.settings import STATIC_DIR
from .utils import find_chinese, get_pinyin_key
import json


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
        if len(words) < 2 or len(words) > 4:
            context['errors'] = ['输入有误，当前只支持双押至四押搜索，且只能为中文搜索。']
        else:
            key = get_pinyin_key(words)
            # read data
            with open(STATIC_DIR + '/data/result.json', 'r') as f:
                rhyme_dict = json.load(f)
            try:
                context['results'] = rhyme_dict[key]
            except KeyError:
                context['errors'] = ['抱歉，词库暂时没有相关押韵词条。']
        return context
