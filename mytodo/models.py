from django.db import models

# Create your models here.
class Task(models.Model):
    class Meta: # DBに関する設定を指定できる内部クラス
        db_table = 'tasks' # 使用するテーブル名を指定
        
    title = models.CharField(verbose_name='タスク名', max_length=255)
    desctiption = models.TextField(verbose_name='詳細', null=True, blank=True)
    complete = models.IntegerField(verbose_name='完了フラグ', default=0)
    start_date = models.DateTimeField(verbose_name='開始日', null=True, blank=True)
    end_date = models.DateTimeField(verbose_name='終了日', null=True, blank=True)
    
    def __str__(self): # 管理画面でレコード毎に表示する文字列を指定
        return f'{self.title}:{self.desctiption}'