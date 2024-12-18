from django.urls import path
from . import views
urlpatterns = [
#  path('', views.oldindex),
#  path('index2/<int:val1>/', views.index2),
#  path('<int:bookId>', views.viewbook),
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name="books.links"),
 path('html5/text/format/', views.text_format, name="books.text.format"),
 path('html5/listing/', views.listing, name="books.listing"),
 path('html5/tables/', views.tables, name="books.tables"),
 path('search/', views.search, name="books.search"),
 path('create/', views.create, name="books.create"),
 path('simple/query/', views.simple_query, name="books.simple_query"),
 path('complex/query/', views.complex_query, name="books.complex_query"),
 path('lab8/task1', views.lte_fifty, name="books.lte_fifty"),
 path('lab8/task2', views.editions_task, name="books.editions_task"),
 path('lab8/task3', views.no_editions_higher, name="books.no_editions_higher"),
 path('lab8/task4', views.order_books, name="books.order_books"),
 path('lab8/task5', views.aggregation, name="books.aggregation"),
 path('lab9_part1/listbooks', views.lab9_list, name="books.lab9_list"),
 path('lab9_part1/addbook', views.lab9_addbook, name="books.lab9_addbook"),
 path('lab9_part1/editbook/<bid>', views.lab9_editbook, name="books.lab9_editbook"),
 path('lab9_part1/deletebook/<bid>', views.lab9_deletebook, name="books.lab9_deletebook"),
 path('lab9_part2/addbook', views.lab9_2_addbook, name="books.lab9_2_addbook"),
 path('lab9_part2/editbook/<bid>', views.lab9_2_editbook, name="books.lab9_2_editbook"),
 path('lab12/task1', views.lab12_task1, name="books.lab12_task1"),
 path('lab12/task2', views.lab12_task2, name="books.lab12_task2"),
 path('lab12/task3', views.lab12_task3, name="books.lab12_task3"),
 path('lab12/task4', views.lab12_task4, name="books.lab12_task4"),
 path('lab12/task5', views.lab12_task5, name="books.lab12_task5"),
]