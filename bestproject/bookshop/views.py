from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from bookshop.forms import CommentForm
from bookshop import models
from bookshop.task import test_fun


logger = logging.getLogger('django')
promise = None

def hello(request):
    global promise
    promise = test_fun.delay(10)
    return HttpResponse("<h2>hello from django</h2>")


def world(request):
    response = {}
    if getattr(promise, "state", False) != "PENDING":
        response = {"promise": promise.get()}
    response['all_books'] = models.Book.objects.all()
    response['comment'] = CommentForm()
    return render(request, './bookshop/index.html', response)


def comment_handler(request, id_book):
    form = CommentForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.comment_book_id = id_book
        obj.save()
        return redirect('world_page')
    return HttpResponse('error')
