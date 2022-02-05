from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class index(ListView):
    model = Post
    template_name = 'index.html'
    category = Category.objects.all()


    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(index, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class articleView(DetailView):
    model = Post
    template_name = 'article.html'

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('article', kwargs={'pk': self.kwargs['pk']}))

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super(articleView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        context["form"] = self.form

        context.update({
            "form": self.form,
            "post_comments" : post_comments,
        })

        like_count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = like_count.total_likes()

        liked = False
        if like_count.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context["liked"] = liked
        return context

    

class addPostView(CreateView):
    model = Post
    # fields = '__all__'
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('index')
    

class addCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'
    success_url = reverse_lazy('index')
    

class updatePostView(UpdateView):
    model = Post
    # fields = ['title', 'title_tag', 'body']
    form_class = EditForm
    template_name = 'update_post.html'
    
    def get_success_url(self, *args, **kwargs):
        return reverse('article', kwargs={'pk': self.kwargs['pk']})

class deletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

def categoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'category.html', {'category' : category.title().replace('-', ' '), 'category_posts' : category_posts})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)

    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class EditProfileView(UpdateView):
    model = User
    fields = ['email', 'first_name', 'last_name']
    template_name = "edit_profile.html"
    success_url = reverse_lazy('index')

class UserProfileView(DetailView):
    model = Profile
    fields = '__all__'
    template_name = 'user_profile.html'