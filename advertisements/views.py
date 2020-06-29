from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Ad


class AdList(ListView):
    model = Ad
    template_name = 'ad/post_list.html'

    def get_queryset(self):
        if self.kwargs.get('category'):
            object_list = Ad.objects.filter(moderated=True, category__slug=self.kwargs.get('category'))
        else:
            object_list = Ad.objects.filter(moderated=True)
        return object_list


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad/detail.html'
    slug_field = 'id'


class SearchResultsView(ListView):
    model = Ad
    template_name = 'ad/post_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Ad.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            moderated=True
        )
        return object_list