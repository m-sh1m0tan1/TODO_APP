from django.shortcuts import render
from django.views import View # クラスベースビューを継承するために必要
from .models import Task

# Create your views here.

class IndexView(View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # todoリストを取得
        todo_list = Task.objects.all()
        context = {
            'todo_list' : todo_list
        }
        
        return render(request, 'mytodo/index.html', context)
    
index = IndexView.as_view()

class AddView(View):
    def get(self, request):
        return render(request, 'mytodo/add.html')
    
    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()
        
        # データが正常であれば
        if is_valid:
            form.save()
            return redirect('/')
        
        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form' : form})
    
add = AddView.as_view()