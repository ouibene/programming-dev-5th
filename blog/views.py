from django.shortcuts import render, redirect
from django.http import HttpResponse

from blog.forms import CommentModelForm, PostModelForm
from blog.models import Post, Comment

from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request): #Post모델이므로 Post를 import한다.

    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list' : post_list #post_list라는 이름으로 index에 넘기겠다는 뜻
        })#render란?

def profile(request):
    return render(request, 'blog/profile.html', {})

def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))

def mysum2(reuqest, x):
    result = sum(int(i) for i in x.split('/'))
    return HttpResponse(result)

def comment_new(request, post_pk):

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == "POST": #최초로 열리는 요청은 get요청. 전송을 누를 때 form태그를 post로 하고 같은 주소(view)에 대해서 method가 처리(?)
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False) #commit=false 는 아직 저장하지 말라는 뜻.
            comment.post = post
            comment.save()
            return redirect(post)

    else:
        form = CommentModelForm()

        #이 부분의 인스턴스는 GET요청으로 오면 빈 내용으로 온 것이고, 실패했을 수도 있음

    # return render(request, 'blog/post_detail.html', {
    #     'form':form,
    #     })
    return redirect(post)


def comment_edit(request, post_pk, pk):
     comment = Comment.objects.get(pk=pk)

     if request.method == 'POST':
         form = CommentModelForm(request.POST, request.FILES, instance=comment)
         if form.is_valid():
             form.save()
             return redirect('/')
     else:
         form = CommentModelForm(instance=comment)

     return render(request, 'blog/comment_form.html', {
         'form': form,
     })


def post_detail(request, pk):

    # try:
    #     post = Post.objects.get(pk=pk) #포스트가 지워질 시 Post.DoesNotExist가 나타남
    # except Post.DoesNotExist:
    #     raise Http404

# 위의 네 줄은 아래의 한 줄과 같은 기능을 한다
    post = get_object_or_404(Post, pk = pk)
    comment_list = Comment.objects.filter(post__pk = pk)

    if request.method == "POST": #최초로 열리는 요청은 get요청. 전송을 누를 때 form태그를 post로 하고 같은 주소(view)에 대해서 method가 처리(?)
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()
            #return redirect('/')
            return redirect(post)
    else:
        form = CommentModelForm()

    return render(request, 'blog/post_detail.html', {
        'post' :post,
        'comment_list' : comment_list,
        'comment_new' : form,
        })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()  # default 는 (commit=True)
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form' : form,
        })