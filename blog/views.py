from django.shortcuts import render
from .models import Post

from django.views.generic import ListView

# Create your views here.
# 포스트 목록 페이지 old
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )

# 포스트 목록 페이지 new ( ListView Class 상속 )
class PostList(ListView):
    model = Post
    ordering = '-pk'
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )