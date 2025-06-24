from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path('', mytodo.index, name='index'), # views.pyのindexを参照
    path('add/', mytodo.add, name='add'),
    path('update_task_complete/', mytodo.Update_task_complete, name='update_task_complete'),
    path('update/<int:id>/', mytodo.UpdateView, name='update'),
    path('delete/<int:id>/', mytodo.DeleteView, name='delete')
]
