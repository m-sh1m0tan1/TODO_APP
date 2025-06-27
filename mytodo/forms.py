from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Task

# Taskモデル用の入力フォーム
class TaskForm(forms.ModelForm):
    class Meta: # 構成や設定を指定できる
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date') # フォームに表示するフィールドを指定
        widgets = { # 特定のフィールドの見た目を設定、日付+時刻入力フィールドになる
            'start_date' : forms.DateTimeInput(attrs={'type' : 'datetime-local'}),
            'end_date' : forms.DateTimeInput(attrs={'type' : 'datetime-local'}),
        }
    
    # initやclean用のメソッドをMetaクラス内に入れてはいけない(自戒)
    
    def __init__(self, *args, **kwargs): # フォーム生成時の初期化処理
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'placeholder' : 'タスク名'} # プレースホルダの指定
        self.fields['description'].widget.attrs = {'placeholder' : '詳細'}
            
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date') # フォームの入力値を安全に取得
        print(f'start_date : {start_date}')
        if start_date and start_date < timezone.now(): # start_dateが存在し、今の時間未満だった場合(要は不正な値かどうか)
            print('開始日を過去に設定することはできません。')
            raise ValidationError('開始日を過去に設定することはできません。')
        return start_date
        
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        print(f'end_date : {end_date}')
        if end_date and end_date < timezone.now():
            print('終了日を過去に設定することはできません。')
            raise ValidationError('終了日を過去に設定することはできません。')
        return end_date
        
        # 全体にバリデーションを追加する場合はcleanメソッドを作成する
    def clean(self):
        cleaned_data = super().clean() # すべての入力データを取得
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')        
        if start_date and end_date and end_date < start_date:
            # print('終了日は開始日より後の日付を設定する必要があります。')
            self.add_error('end_date', '終了日は開始日より後の日付を設定する必要があります。')