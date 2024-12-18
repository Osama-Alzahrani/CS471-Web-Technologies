from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg
from .forms import BookForm


def oldindex (request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/oldindex.html",{"name":name})

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 if targetBook == None:
    return render(request, 'static/404.html')
    
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

 

def index2(request, val1 = 0): #add the view function (index2) 
   return HttpResponse("value1 = "+str(val1))


def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book = 123
 if bookId == book1["id"]:
   book = book1
 elif bookId == book2["id"]:
   book = book2
 return render(request, 'bookmodule/one_book.html',{"book":book})


def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def links(request):
  return render(request, 'bookmodule/html5/links.html')

def text_format(request):
  return render(request, 'bookmodule/html5/text.html')

def listing(request):
  return render(request, 'bookmodule/html5/listing.html')

def tables(request):
  return render(request, 'bookmodule/html5/tables.html')

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def search(request):
  if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
    # now filter
    books = __getBooksList()
    newBooks = []
    for item in books:
      contained = False
      if isTitle and string in item['title'].lower(): contained = True
      if not contained and isAuthor and string in item['author'].lower():contained = True

      if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})

  return render(request, 'bookmodule/search.html')


def create(request):
  mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley',price=50.0, edition = 1)
  mybook.save()
  return HttpResponse('Book created successfully')


def simple_query(request):
  mybooks=Book.objects.filter(title__icontains='a') # <- multiple objects
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
  mybooks = Book.objects.filter(author__isnull = False).filter(title__icontains='a').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
  if len(mybooks)>=1:
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})
  else:
    return render(request, 'bookmodule/index.html')

def lte_fifty(request):
  
  mybooks = Book.objects.filter(Q(price__lte = 50))
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def editions_task(request):
  mybooks = Book.objects.filter(Q(edition__gt = 2) & (Q(title__contains = "an") | Q(author__contains = "an"))) #Since my authors and title doesn't contain qu : |
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def no_editions_higher(request):
  mybooks = Book.objects.filter(~(Q(edition__gt = 2) & (Q(title__contains = "an") | Q(author__contains = "an")))) #Since my authors and title doesn't contain qu : |
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def order_books(request):
  mybooks = Book.objects.order_by('title')
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def aggregation(request):
  agg1 = Sum('price' , default=0)
  agg2 = Avg('price' , default=0)
  agg3 = Max('price' , default=0)
  agg4 = Min('price' , default=0)
  query = Book.objects.aggregate(Sum = agg1, Average=agg2, Max=agg3, Min=agg4, Count=Count('id'))

  return render(request, 'bookmodule/statistics.html', {'data':query})

def lab9_list(request):
  books = Book.objects.all()
  return render(request, 'bookmodule/bookList.html', {'books':books})

def lab9_addbook(request):
  if request.method=='POST':
    title=request.POST.get('title')
    price=request.POST.get('price')
    edition=request.POST.get('edition')
    author=request.POST.get('author')
    obj = Book(title=title, price = float(price), edition = edition, author = author)
    obj.save()
    return redirect('books.lab9_list')
  return render(request, 'bookmodule/createBook.html')

def lab9_editbook(request, bid):
  obj = Book.objects.get(id = bid)
  if request.method == 'POST':
    title=request.POST.get('title')
    price=request.POST.get('price')
    edition=request.POST.get('edition')
    author=request.POST.get('author')
    obj.title = title
    obj.price = float(price)
    obj.edition = int(edition)
    obj.author = author
    obj.save()
    return redirect('books.lab9_list')
  return render(request, "bookmodule/updateBook.html", {'book':obj})

def lab9_deletebook(request, bid):
  obj = Book.objects.get(id = bid)
  if request.method=='POST':
    obj.delete()
    return redirect('books.lab9_list')
  return render(request, "bookmodule/deleteBook.html", {'obj':obj})

def lab9_2_addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('books.lab9_list')
    else:
        form = BookForm()
    return render(request, "bookmodule/forms/addBook.html", {'form': form})

def lab9_2_editbook(request, bid):
  obj = Book.objects.get(id = bid)
  if request.method=='POST':
    form = BookForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
      print("Form is valid")
      print("File data:", request.FILES.get('coverPage'))
      form.save()
      return redirect('books.lab9_list')
  else: 
    form = BookForm(instance = obj)
  return render(request, "bookmodule/forms/update.html", {'form':form})

def lab12_task1(request):
  return render(request, "bookmodule/js/task1.html")

def lab12_task2(request):
  return render(request, "bookmodule/js/task2.html")

def lab12_task3(request):
  return render(request, "bookmodule/js/task3.html")

def lab12_task4(request):
  return render(request, "bookmodule/js/task4.html")

def lab12_task5(request):
  return render(request, "bookmodule/js/task5.html")