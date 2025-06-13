from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task) # 作成したモデルを管理サイト(admin)に追加