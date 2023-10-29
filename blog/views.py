from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import BlogPostForm
from .models import BlogPost


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    template_name = 'blog/blog_create.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')
    extra_context = {'title': 'Добавить пост'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class BlogUpdateView(generic.UpdateView):
    model = BlogPost
    template_name = 'blog/blog_update.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blogs')


class BlogListView(generic.ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наши блоги'
        return context


class BlogDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

class BlogPublishView(generic.View):
    def get(self, request, pk):
        blog = get_object_or_404(BlogPost, pk=pk)
        if request.user.is_staff and blog.is_active == False:
            blog.is_active = True
            blog.save()
        else:
            blog.is_active = False
            blog.save()
        return redirect('blog:blogs')