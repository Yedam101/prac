from django.shortcuts import render, redirect
from .models import Post, Comment


def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }

    return render(request, "post_list.html", context)


def post_detail(request, isthis):
    detail = Post.objects.get(id=isthis)
    context = {
        "detail":detail
    }

    if request.method == "POST":
        comment = request.POST["comment-content"]
        Comment.objects.create(
            post_id=isthis,
            content=comment
        )

    return render(request, "post_detail.html", context)


def post_upload(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"]

        new_post = Post.objects.create(
            title=title, 
            content=content,
            thumbnail=thumbnail,
            )
        return redirect(f"/post/{new_post.id}")
    
    return render(request, "post_upload.html")


def post_update(request, isthis):
    detail = Post.objects.get(id=isthis)
    context = {
        "detail":detail
    }

    if request.method == "POST":
        # 썸네일이 제출되었는지 확인
        thumbnail_file = request.FILES.get('thumbnail', None)
        
        # 제출되지 않았다면 기존 썸네일을 사용
        if not thumbnail_file:
            thumbnail_file = detail.thumbnail

        detail.title = request.POST["title"]
        detail.content = request.POST["content"]
        detail.thumbnail = thumbnail_file
        detail.save()

        return redirect(f"/post/{detail.id}")

    return render(request, "post_update.html", context)


def post_delete(request, isthis):
    post_to_delete = Post.objects.get(id=isthis)
    post_to_delete.delete()
    
    return redirect("/post/") 
