from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from django_filters.views import FilterView

from .filters import AdFilter
from .forms import AddPost, SendMailForm
from .models import Ad
from .task import send_verification_email


class AdList(ListView):
    model = Ad
    template_name = 'ad/post_list.html'
    paginate_by = 6

    def get_queryset(self):
        if self.kwargs.get('category'):
            object_list = self.model.objects.filter(moderated=True, category__slug=self.kwargs.get('category'), status=False)
        else:
            object_list = self.model.objects.filter(moderated=True, status=False)
        return object_list


# Надо доработать, похоже на копирование кода
class UserAdList(ListView):
    model = Ad
    template_name = 'ad/post_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = self.model.objects.filter(author=self.request.user)
        return queryset


class AdDetail(FormView, DetailView):
    model = Ad
    template_name = 'ad/detail.html'
    slug_field = 'id'
    form_class = SendMailForm
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        send_verification_email.delay(email, message)
        form.save()
        return super().form_valid(form)


class SearchResultsView(FilterView):
    model = Ad
    template_name = 'ad/post_list.html'
    filterset_class = AdFilter

    # def get_queryset(self):
    #     # query = self.request.GET.get('q')
    #     object_list = filter
    #     return object_list


class NewPostView(CreateView):
    model = Ad
    form_class = AddPost
    template_name = 'ad/add_post.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super(NewPostView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewPostView, self).form_valid(form)


class EditPost(UpdateView):
    model = Ad
    form_class = AddPost
    template_name = 'ad/add_post.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("Нет прав для редактирования")
        return super(EditPost, self).dispatch(request, *args, **kwargs)
