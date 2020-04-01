from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging
from bookshop.forms import CommentForm
from bookshop import models

logger = logging.getLogger('django')


def hello(request):
    logger.error('hello error')
    return HttpResponse("<h2>hello from django</h2>")


def world(request):
    response = {}
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
