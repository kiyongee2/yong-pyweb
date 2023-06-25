from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.utils import timezone

def index(request):
    # 최신글 3개 보여주기
    recent_post = Post.objects.order_by('-pub_date')[0:3]
    context = {'recent_post': recent_post}
    return render(request, 'blog/index.html', context)

# 포스트 목록
def post_list(request):
    post_list = Post.objects.order_by('-pub_date')

    # 페이지
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    page_obj = paginator.get_page(page)

    categories = Category.objects.all()
    context = {'post_list': page_obj, 'categories': categories}
    return render(request, 'blog/post_list.html', context)

# 포스트 상세 페이지
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    categories = Category.objects.all()
    context = {'post': post, 'categories': categories}
    return render(request, 'blog/detail.html', context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)

# 카테고리 페이지
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug)
    post_list = Post.objects.filter(category=current_category) #현재 카테고리의 포스트
    post_list = post_list.order_by('-pub_date')  #날짜순 내림 차순
    categories = Category.objects.all()
    context = {
        'current_category': current_category,
        'post_list': post_list,
        'categories': categories
    }
    return render(request, 'blog/post_list.html', context)

# 포스트 삭제
@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')

