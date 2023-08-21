from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
    '''
    1. 이미 사용자가 브라우저에서 로그인을 했다면 피드 페이지
    2. 로그인 안 되어있다면(로그아웃을 했다면) 로그인 페이지 
    '''
    if request.user.is_authenticated:
        return redirect("/posts/feeds/")
    
    # 로그인 시도 시 
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        # LoginForm에 전달된 데이터가 유효하다면(db에 있냐와는 별개)
        if form.is_valid():
            uid = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]

            # 여기서 db에 있는지 검사
            user = authenticate(username=uid, password=pw)
            if user:
                login(request, user)
                return redirect("/posts/feeds/")
            else:
                form.add_error(None, "사용자가 없습니다.")
        
        # 어떤 경우든 실패한 경우(데이터검증, 사용자 검사) 다시 로그인 페이지 렌더링
        # 이 때 이전 POST에서 보낸 데이터 값 사용
        context = {
            "form": form
        }
        return render(request, "users/login.html", context)
    

    else:
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, "users/login.html", context)
    


def logout_view(request):
    # logout 함수에 request 전달하여 호출
    logout(request)

    return redirect("/users/login/")
