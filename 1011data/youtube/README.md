# Many to one relationships 01

## ForeignKey

### models
```py
from django.conf import settings
class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE )
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    else...
```

## shell_plus

