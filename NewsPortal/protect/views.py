from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import Author


class IndexView(TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not Author.objects.filter(user=self.request.user).exists()
        return context
