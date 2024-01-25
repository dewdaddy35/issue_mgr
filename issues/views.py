from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
    )


class PostListView(ListView):
    template_name ="issues/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Post
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        post = self.get_object()
        return post.developer == self.request.user