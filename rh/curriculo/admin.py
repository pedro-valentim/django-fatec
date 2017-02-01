from django.contrib import admin
from .models import Aluno, Curriculo


class CurriculoAdmin(admin.ModelAdmin):
    pass


class AlunoAdmin(admin.ModelAdmin):
    fields = ('nome', )
    readonly_fields = ('datacadastro',)

    # def datacadastro(self, obj):
    #     return obj.datacadastro

    # datacadastro.empty_value_display = '???'


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curriculo, CurriculoAdmin)
