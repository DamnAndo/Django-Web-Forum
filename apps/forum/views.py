from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .models import Forum

@method_decorator(login_required,name="dispatch")
class ForumCreate(CreateView):
    model = Forum
    fields = ['title','desc']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
