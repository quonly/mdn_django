from django.contrib import admin
from .models import Book,BookInstance,Author,Genre

class BookInline(admin.TabularInline):
  model = Book
  extra = 0

class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name','first_name','date_of_birth','date_of_death')
  fields = ['first_name','last_name',('date_of_birth','date_of_death')]
  inlines = [BookInline]

class BookInstanceInline(admin.TabularInline):
  model = BookInstance

class BookAdmin(admin.ModelAdmin):
  list_display = ('title','author','display_genre')
  
  inlines = [BookInstanceInline]
  extra = 0

class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('id','book','status','due_back')
  list_filter = ('status','due_back')
  fieldsets = (
    (None,{
      'fields':('book','imprint','id')
    }),
    ('Availability',{
      'fields':('status','due_back')
    })
  )
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)