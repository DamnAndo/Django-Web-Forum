from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from  django.utils.decorators import method_decorator
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Forum,Comment
from .forms import CommentForm

class OwnerMixin(object):
    def dispatch(self, request,*args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class ForumListView(ListView):
    model=Forum
    context_object_name = 'forums'
    paginate_by = 3
    queryset = Forum.objects.order_by("-created_at")

class ForumUserListView(ListView):
    def get_queryset(self):
        self.user = get_object_or_404(User,username=self.kwargs['username'])
        return Forum.objects.filter(user = self.user)

class ForumDetailView(DetailView):
    model=Forum
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # context['forum_list'] = Forum.objects.all()
        context['form_comment'] = CommentForm()
        return context

@method_decorator(login_required,name="dispatch")
class ForumUpdateView(OwnerMixin,UpdateView):
    model=Forum
    fields = ['title','desc']
    success_message = "Success Update Forum"
    template_name = "forum/forum_update_form.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy('forum-detail', kwargs={'slug': self.object.slug})


class CommentUpdate(OwnerMixin,UpdateView):
    model = Comment
    fields = ['desc']
    template_name = "forum/comment_update_form.html"

@method_decorator(login_required,name='dispatch')
class ForumDeleteView(DeleteView):
    model = Forum
    success_url = '/forum'


@method_decorator(login_required,name="dispatch")
class ForumCreate(SuccessMessageMixin,CreateView):
    model = Forum
    fields = ['title','desc']
    success_message = "Success Create Forum"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required,name="dispatch")
class CommentCreate(CreateView):
    model = Comment
    fields = ['desc']

    def form_valid(self, form):
        _forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.forum = _forum
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    success_url = '/forum'