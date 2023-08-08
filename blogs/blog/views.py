from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.forms import PostForm, CommentForm
from blog.models import Post, Category, Comment

def index(request):
    # 최신글 3개 보여주기
    recent_post = Post.objects.order_by('-pub_date')[0:3]
    context = {'recent_post': recent_post}
    return render(request, 'blog/index.html', context)

# 포스트 목록
def post_list(request):
    post_list = Post.objects.order_by('-pub_date') # 포스트 전체 검색
    total_post = len(post_list)  # 전체 게시글 수

    # 검색
    kw = request.GET.get('kw', '')
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()

    # 페이지
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    page_obj = paginator.get_page(page)

    categories = Category.objects.all()  # 전체 카테고리

    context = {
        'post_list': page_obj,
        'categories': categories,
        'total_post': total_post,
        'kw': kw
    }
    return render(request, 'blog/post_list.html', context)

# 상세 페이지
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()  # 카테고리 전체 검색
    post_all = Post.objects.all()  # 전체 게시글
    total_post = len(post_all)

    context = {'post': post, 'categories': categories, 'total_post': total_post}
    return render(request, 'blog/detail.html', context)

# 글쓰기
@login_required(login_url='common:login')
def post_create(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) #(일반속성, 파일)
        if form.is_valid(): #유효하다면
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # 현재 시간
            post.author = request.user  #로그인한 사람이 글쓴이임
            post.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()  #비어있는 폼
    context = {'form': form, 'categories': categories}
    return render(request, 'blog/post_form.html', context)

# 카테고리별 페이지 처리 메서드
def category_page(request, slug):
    current_category = Category.objects.get(slug=slug) #현재 카테고리 검색
    post_list = Post.objects.filter(category=current_category) # 현 카테고리의 포스트들
    post_list = post_list.order_by('-pub_date')  #날짜순 내림차순
    categories = Category.objects.all() #전체 카테고리

    post_all = Post.objects.all()  #전체 게시글
    total_post = len(post_all)

    # 검색
    kw = request.GET.get('kw', '')
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()

    # 페이지
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    page_obj = paginator.get_page(page)

    context = {
        'current_category': current_category,
        'post_list': page_obj,
        'categories': categories,
        'total_post': total_post,
        'kw': kw
    }
    return render(request, 'blog/post_list.html', context)

# 포스트 삭제
@login_required(login_url='common:login')
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')

# 포스트 댓글 등록
@login_required(login_url='common:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.pub_date = timezone.now()
            comment.post = post
            comment.save()
    return redirect('blog:detail', post_id=post_id)

# 포스트 댓글 삭제
@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('blog:detail', post_id=comment.post_id)

# 포스트 댓글 수정
@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('blog:detail', post_id=comment.post_id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'blog/comment_form.html', context)

