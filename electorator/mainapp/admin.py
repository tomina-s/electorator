from django.contrib import admin
from .models import Candidate
# Register your models here.


class CandidateAdmin(admin.ModelAdmin):
    '''Класс полей модели Candidate , которые можно будет видеть в админке, работая с моделью.'''

    # мб надо будет подкорректировать
    list_display = ('id', 'name', 'info', 'sum_votes')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'info')
    list_editable = ('sum_votes',)
    list_filter = ('sum_votes',)


admin.site.register(Candidate, CandidateAdmin)
