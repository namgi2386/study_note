from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

# django는 User모델을 직접 참조하는 것을 권장하지 않는다.
from .models import User
# 그래서 django는 User모델의 간접적 참조방법을 제공한다.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name','email',)
