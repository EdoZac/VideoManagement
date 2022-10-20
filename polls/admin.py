from django.contrib import admin

from .models import Choice, Movie, Author, Genre


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Author)
admin.site.register(Genre)