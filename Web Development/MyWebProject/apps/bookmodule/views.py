from django.shortcuts import render
from django.http import HttpResponse

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