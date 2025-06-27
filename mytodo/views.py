from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

# from .forms import TaskForm

# Create your views here.

class IndexView(View):
    def get(self, request): # GETリクエストが送信された時に呼び出される
        # todoリストを取得
        todo_list = Task.objects.filter(complete=0)
        todo_checked_list = Task.objects.filter(complete=1)
        context = {
            'todo_list' : todo_list,
            'todo_checked_list' : todo_checked_list,
        }
        
        return render(request, 'mytodo/index.html', context)
    
index = IndexView.as_view()

class AddView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'mytodo/add.html', {'form' : form})
    
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

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        # print(args)
        # print(kwargs)
        task_id = request.POST.get('task_id')
        # print(task_id)
        task = Task.objects.get(id=task_id)
        # print(task)
        task.complete = not task.complete
        task.save()
        
        return redirect('/')
    
Update_task_complete = Update_task_complete.as_view()

class UpdateView(View):
    model = Task
    template_name = 'mytodo/update.html'
    fields = ['title', 'description', 'start_date', 'end_date']
    def get(self, request, id):
        task = Task.objects.get(id = id)
        form = TaskForm(initial={'title' : task.title, 'description' : task.description, 'start_date' : task.start_date, 'end_date' : task.end_date})
        return render(request, 'mytodo/update.html', {'form' : form, 'task' : task})
        
    def post(self, request, id, *args, **kwargs):  # URLからクエリパラメータを送って変数id(idは選択したデータのid)に格納
        # print(f'id:{id}')
        data = Task.objects.get(id=id)  # idをもとにTaskモデルからデータを抽出
        form = TaskForm(request.POST, instance=data) # 引数instanceに抽出してきたデータを渡すことでひな形を持った状態で新しいデータの上書きができる、新規作成でなく更新できるようになる
        is_valid = form.is_valid()
        if is_valid:
            form.save() # 上書きしたデータを保存
            return redirect('/')
        return render(request, 'mytodo/update.html', {'form' : form})
    
UpdateView = UpdateView.as_view()

class DeleteView(View):
    def get(self, request, id):
        task_data = Task.objects.get(id = id)
        print(task_data.title)
        # form = TaskForm()
        # task_data = Task.objects.get(id = id)
        return render(request, 'mytodo/delete.html', {'title' : task_data.title, 'id' : id})
    
    def post(self, request, id):
        task_data = Task.objects.get(id = id)
        form = TaskForm(instance=task_data)
        Task.objects.filter(id = id).delete()
        return redirect('/')
    
DeleteView = DeleteView.as_view()