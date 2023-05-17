from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
  """View function for home page of site."""

  # Generate counts of some of the main objects
  num_books = Book.objects.all().count()
  num_instances = BookInstance.objects.all().count()
  
  # Available books (status = 'a')
  # __ double underscore trailing fields name is called lookup 
  # exact = exact match
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()
  
  # The 'all()' is implied by default. = all() จะถูกเรียกใช้เป็นค่าเริ่มต้น เราจึงไม่ต้องเรียก all() ก็ได้
  num_authors = Author.objects.count()

  # Chellenge
  num_genres = Genre.objects.count()
  num_books_title_l = Book.objects.filter(title__icontains='l').count()
  
  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_genres': num_genres,
    'num_books_title_l': num_books_title_l,
  }
  
  # Render the HTML template index.html with the data in the context variable
  return render(request,'index.html',context=context)

class BookListView(generic.ListView):
  model = Book
  context_object_name = 'book_list'
  paginate_by = 1

class BookLoveListView(generic.ListView):
  model = Book
  context_object_name = 'love_list'
  queryset = Book.objects.filter(title__icontains='love')[:5] # Get 5 books containing the title love
  template_name = 'catalog/books/love.html' # Specify your own template name/location
  
class BookDetailView(generic.DetailView):
  model = Book