from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, PublishingHouse
from django.template import loader
from django.shortcuts import redirect

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    my_range =[i for i in range(1,101)]
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "my_range": my_range,
    }
    
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')

def ph(request):
    template = loader.get_template('publishing_house.html')
    ph_list = PublishingHouse.objects.all()
    data = {
        "ph_list": ph_list,
    }
    return HttpResponse(template.render(data, request))