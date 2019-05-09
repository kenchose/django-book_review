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
        all_reviews = Review.objects.all().order_by('-id')[:6]
        all_books = Book.objects.all().order_by('-id')[6:]
        other_reviews = Review.objects.all().order_by('-id')[6:]
        context = {
            'curr_user': user,
            'users': all_users,
            'reviews': all_reviews,
            'books': all_books,
            'other_r': other_reviews,
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
            return redirect ('/#val')
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
                return redirect('/#val')
        except:
            user = User.objects.logUser(request.POST)
            request.session['id']=user.id
            return redirect ('/home')
    else:
        return redirect ('/')

def newAdd(request):
    if not request.session['id']:
        return redirect('/')
    else:
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
            result = Review.objects.addBookReview(request.POST, curr_user, request.FILES)
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
        'curr_user': curr_user
    }
    return render(request, 'book_review/book_show.html', context)

def user(request, user_id):
    curr_user = User.objects.get(id=request.session['id'])
    user = User.objects.get(id=user_id)
    reviews = Review.objects.filter(writer=user)
    count = reviews.count()
    context = {
        'curr_user': curr_user,
        'user': user,
        'reviews': reviews,
        'count': count
    }
    return render (request, 'book_review/user.html', context)

def edit_user(request, user_id):
    curr_user=User.objects.get(id=request.session['id'])
    user = User.objects.get(id=user_id)
    if curr_user.id == user.id:
        context = {
            "curr_user": curr_user
        }
        return render(request, 'book_review/edit.html', context)
    else:
        error.append("You cannot edit other user's profile information.")
        if error:
            for error in error:
                messages.error(request, error)
                return redirect('/user/{}'.format(user_id))

def update_user(request, user_id):
    if request.method == 'POST':
        curr_user=User.objects.get(id=user_id)
        validation=User.objects.editVal(request.POST, request.FILES, curr_user)
        if len(validation) > 0:
            for error in validation:
                messages.error(request, error)
            return redirect ('/edit/{}'.format(user_id))
        else:
            curr_user = User.objects.updateUser(request.POST, request.FILES, curr_user)
            messages.success(request, "Your information have been successfully updated.")
            return redirect ('/user/{}'.format(curr_user.id))
    else:
        return redirect ('/edit/{}'.format(user_id))


def add_review(request, book_id):
    if request.method == 'POST':
        curr_user=User.objects.get(id=request.session['id'])
        book=Book.objects.get(id=book_id)
        validation=Review.objects.addReviewVal(request.POST, book, curr_user)
        if validation > 1:
            for error in validation:
                messages.error(request, error)
            return redirect ('/books/{}'.format(book_id))
        else:
            user = User.objects.get(id=request.session['id'])
            book = Book.objects.get(id=book_id)
            result = Review.objects.addReview(request.POST, book, user)
            return redirect('/books/{}'.format(result.book_id))
    else:
        return redirect('/books/{}'.format(book_id))


def delete(request, review_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['id'])
        review = Review.objects.get(id=review_id)
        validation = User.objects.deleteVal(review, user)
        if len(validation) > 0:
            for error in valication:
                messages.error(request, errro)
            return redirect ("/books/{}".format(self.review_id))
        else:
            review_id.delete()
            return redirect ("/books/{}".format(self.review_id.book.id))
            # return redirect ("/book/{}".format(self.review_id)
    else:
        return redirect ("/books/{}".format(self.review_id.book.id))

def confirmation(request, review_id):
    r = Review.objects.get(id=review_id)
    book = r.book.id
    r.delete()
    return redirect ("/books/{}".format(book))

def logout(request):
    request.session.clear()
    messages.success(request, "You've been successfully logged out.")
    return redirect('/')
    
