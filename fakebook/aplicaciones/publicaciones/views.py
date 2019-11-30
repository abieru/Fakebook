from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post


@method_decorator(staff_member_required, name="dispatch")
class PostCreate(CreateView):
	model = Post
	form_class = PostForm
	success_url = reverse_lazy('post:posts')


@method_decorator(staff_member_required, name="dispatch")
class PostUpdate(UpdateView):
	model = Post
	form_class = PostForm
	template_name_suffix = '_update_form'
	
	def get_success_url(self):
		return reverse_lazy('post:update', args=[self.object.author, self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:posts')