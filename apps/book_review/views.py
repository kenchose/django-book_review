# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from . models import *

def index(request):
    return render(request, 'book_review/index.html')

def home (request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        all_users = User.objects.all()
        all_reviews = Review.objects.all().order_by('-id')[:3]
        all_books = Book.objects.all()
        context = {
            'curr_user': user,
            'users': all_users,
            'reviews': all_reviews,
            'books': all_books
        }
        return render(request, 'book_review/home.html', context)
    else:
        return redirect ('/')

def register(request):
    if request.method == 'POST':
        result = User.objects.registerVal(request.POST)
        if len(result) > 0:
            for error in result:
                messages.error(request, error)
            return redirect ('/')
        else:
            newUser = User.objects.newUser(request.POST)
            request.session['id'] = newUser.id
            return redirect('/home')
    else:
        return redirect ('/')

def login(request):
    if request.method == 'POST':
        result=User.objects.logVal(request.POST)
        try:
            if len(result) > 0:
                for error in result:
                    messages.error(request, error)
                return redirect('/')
        except:
            user = User.objects.logUser(request.POST)
            request.session['id']=user.id
            return redirect ('/home')
    else:
        return redirect ('/')

def newAdd(request):
    all_authors = Author.objects.all()
    curr_user = User.objects.get(id=request.session['id'])
    context = {
        'authors': all_authors,
        'curr_user': curr_user,
    }
    return render(request, 'book_review/add.html', context)

def add(request):
    if request.method == 'POST':
        curr_user = User.objects.get(id=request.session['id'])
        validation = Review.objects.addBookReviewVal(request.POST)
        if len(validation) > 0:
            for error in validation:
                messages.error(request, error)
            return redirect ('/books/add')
        else:
            result = Review.objects.addBookReview(request.POST, curr_user)
            return redirect ('/books/{}'.format(result.book.id))
    else:
        return redirect ('/books/add')

def book(request, book_id): 
    curr_user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    context = {
        'curr_book': book,
        'book_reviews': reviews,
        'user': curr_user
    }
    return render(request, 'book_review/book_show.html', context)

def user(request, user_id):
    user = User.objects.get(id=user_id)
    reviews = Review.objects.filter(writer=user)
    count = reviews.count()
    context = {
        'user': user,
        'reviews': reviews,
        'count': count
    }
    return render (request, 'book_review/user.html', context)

def add_review(request, book_id):
    if request.method == 'POST':
        if len(request.POST['content']) < 1:
            messages.error(request, 'Nothing to submit')
            return redirect ('/books/{}'.format(book_id))
        else:
            user = User.objects.get(id=request.session['id'])
            book = Book.objects.get(id=book_id)
            result = Review.objects.addReview(request.POST, book, user)
            return redirect('/books/{}'.format(result.book_id))
    else:
        return redirect('/books/{}'.format(book_id))


def delete(request, review_id):
    user = User.objects.get(id=request.session['id'])
    review = Review.objects.get(id=review_id)
    context = {
        'user':user,
        'review':review
    }
    return render(request, 'book_review/delete.html', context)

def confirmation(request, review_id):
    r = Review.objects.get(id=review_id)
    book = r.book.id
    r.delete()
    return redirect ("/books/{}".format(book))

def logout(request):
    request.session.clear()
    messages.success(request, "You've been successfully logged out.")
    return redirect('/')
    
