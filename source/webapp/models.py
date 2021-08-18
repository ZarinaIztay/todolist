from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Type')

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Status')

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.CASCADE, verbose_name='Status')
    type = models.ForeignKey('webapp.Type', related_name='tasks', on_delete=models.CASCADE, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return '{}: {}, {}'.format(self.title, self.type, self.status)
