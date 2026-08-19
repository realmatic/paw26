from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Record, Procedure, Note, Material, Tool, Supply

class SupplyInline(admin.TabularInline):
    model = Supply
    extra = 1

class ProcedureInline(admin.TabularInline):
    model = Procedure
    extra = 1
    min_num = 0
    max_num = 10
    fields = ['sequence', 'procedure_text']

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'sequence':
            #import logging
            #logger = logging.getLogger('app')
            #logger.info(db_field.name)
            kwargs['widget'] = TextInput(attrs={'size': '3'})
        if db_field.name == 'procedure_text':
            kwargs['widget'] = TextInput(attrs={'size': '60'})
        return super().formfield_for_dbfield(db_field, **kwargs)

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
    min_num = 0
    max_num = 10
    fields = ['note_text']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
    #    models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }

class RecordAdmin(admin.ModelAdmin):
    list_display = ["title","production_date","status"]

    inlines = [SupplyInline, ProcedureInline, NoteInline]


admin.site.register(Record, RecordAdmin)
admin.site.register(Tool)
admin.site.register(Material)