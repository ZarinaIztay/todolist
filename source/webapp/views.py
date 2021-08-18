from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from webapp.models import Type, Status, Task
from webapp.forms import TaskForm


class IndexView(TemplateView):
    template_name = 'task/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return context


class CreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('task_view', task_pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})


class EditView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'type': task.type,
        })
        return render(request, 'task/update.html', context={'form': form, 'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        form = TaskForm(data=request.POST)
        print(task)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', task_pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task})


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['task_pk'])
        task.delete()
        return redirect('index')


