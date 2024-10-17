# Authentication SYSTEM 02

## 목차

[1. 회원가입](#회원가입)  
[2. 회원탈퇴](#회원탈퇴)  
[3. 회원정보수정](#회원정보수정)  
[4. 비밀번호변경](#비밀번호변경)  
[5. 로그인 사용자에 대한 접근제한](#로그인-사용자에-대한-접근제한)  
[6. 참고](#참고)  

---

## 회원가입

### accounts/urls

```py
path('signup/', views.signup, name='signup'),
```

### views.py

```py
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CustomUserCreationForm , CustomUserChangeForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html' , context)
```

### signup.html

> login.html 복붙 後
> action주소변경

### accounts/forms

```py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

```

### articles/index.html
```html
<a href="{% url "accounts:signup" %}">SIGNUP</a>
```


## 회원탈퇴

### accounts/urls

```py
path('delete/', views.delete, name='delete'),
```

### views
```py
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

### articles/index.html
```html
  <form action="{% url "accounts:delete" %}" method='post'>
    {% csrf_token %}
    <input type="submit" value="탈퇴">
  </form>
```

## 회원정보수정

### update.html

> login.html 복붙 後
> action주소변경

### accounts/urls
```py
    path('update/', views.update, name='update'),
```

### forms.py
```py
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name','email',)

```

### views
```py
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request , 'accounts/update.html' , context)
```

### articles/index.html
```html
  <a href="{% url "accounts:update" %}">회원정보수정</a>
```

## 비밀번호변경

### CRUD/urls
```py
from accounts import views
path('<int:user_pk>/password' , views.change_password , name='change_password')
```

### views
```py
from django.contrib.auth.forms import PasswordChangeForm
def change_password(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/change_password.html',context)
```

### change_password.html
```html
    <h1>비밀번호 변경</h1>
    <form action="{% url "change_password" user.pk %}" method="post">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit">
    </form>
```

## 로그인 사용자에 대한 접근제한

### views
```py
from django.contrib.auth import update_session_auth_hash
def change_password(request,user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user , request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/change_password.html',context)
```

### index.html
메인화면 내용변경
```html
  {% if request.user.is_authenticated %}
  <p>안녕하세요 {{ user.username }}</p>
  <form action="{% url "accounts:logout" %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="LOGOUT">
  </form>
  <form action="{% url "accounts:delete" %}" method='post'>
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
  </form>
  <a href="{% url "accounts:update" %}">회원정보수정</a>
  {% else %}
  <a href="{% url "accounts:login" %}">LOGIN</a>
  <a href="{% url "accounts:signup" %}">회원가입</a>
  {% endif %}
```

### views.login & views.signup
```py 
# 아래내용 추가
    if request.user.is_authenticated():
        return redirect('articles:index')
```

### articles/views & accounts/views
```py
from django.contrib.auth.decorators import login_required
@login_required 
#적절히 추가하기
# logout 
# delete
# update
# change_password

# create
# delete
# update
```

## 참고

### 회원가입 후 로그인 accounts/views
```py
if form.is_valid():
    # form.save() # 삭제
    user = form.save() # 추가 
    auth_login(request, user) # 추가
    return redirect('articles:index')
```

### 회원탈퇴 후 로그아웃 accounts/views
```py
    request.user.delete()
    auth_logout(request) # 추가
    return redirect('articles:index')
```