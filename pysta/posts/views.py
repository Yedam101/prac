from django.shortcuts import render, redirect

def feeds(request):
    '''
    # request로부터 사용자 정보 가져옴
    user = request.user
    is_authenticated = user.is_authenticated

    if not is_authenticated:
        return redirect("/users/login/")
    '''
    if not request.user.is_authenticated:
        return redirect("/users/login/")

    return render(request, "posts/feeds.html")
