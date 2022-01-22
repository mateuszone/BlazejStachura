from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import ListView

from blog.models import Post
from www.forms import EmailPostForm


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post,
#                              status='published',
#                              publish__year=year,
#                              publish__month=month,
#                              publish__date=day)
#     return render(request, 'blog/detail.html', {'post': post})


# class post_detail(View):
#     def get(self, request, year, month, day, post):
#         post = get_object_or_404(Post, slug=post,
#                                  status='published',
#                                  publish__year=year,
#                                  publish__month=month,
#                                  publish__date=day)
#         return render(request, 'blog/detail.html', {'post': post})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # pobieranie posta na podstawie jego identyfikatora
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} {{}} zachęca do przeczytania "{}"'.format(cd['name'], cd['email'], post.title)
            message = f'Przeczytaj post "{post.title}" na stronie {post_url}' \
                      f'\n\n Komentarz dodany przez {cd["name"]} : {cd["email"]}'
            EMAIL_HOST = 'smtp.gmail.com'
            EMAIL_HOST_USER = 'twoja_nazwa_konta_uzytkownika'
            EMAIL_HOST_PASSWORD = 'twoje haslo'
            EMAIL_PORT = 587
            EMAIL_USE_TLS = True
            print(cd)
            send_mail(subject, message, 'mateuszczaja086@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent
                                                    })
