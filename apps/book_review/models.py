# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt



class UserManager(models.Manager):
    def registerVal(self, postData):
        error=[]
        if len(postData['name']) < 1 or len(postData['alias']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1:
            error.append('All fields cannot be empty.')
        try:
            validate_email(postData['email'])
        except ValidationError as e:
            error.append("Email must be a valid email.")
        if len(postData['email']) < 1:
            error.append('Email must be more than 2 characters long.')
        if User.objects.filter(email__iexact=postData['email']):
            error.append('Email is already registered.')
        if len(postData['name']) < 1:
            error.append('Name must be more than 2 characters long.')
        if len(postData['alias']) < 1:
            error.append('Alias must be more than 6 characters long.')
        if len(postData['password']) < 1:
            error.append('Password must be at least 8 characters long.')
        if postData['password'] != postData['password_confirmation']:
            error.append('Password and password confirmation does not match.')
        return error

    def newUser(self, postData):
        hashed_pw=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        new_user=User.objects.create(name=postData['name'], alias=postData['alias'], email=postData['email'], password=hashed_pw)
        return new_user

    def logVal(self, postData):
        error=[]
        retrieved_users=User.objects.filter(email=postData['email'])
        if len(retrieved_users) > 0:
            retrieved_user=retrieved_users[0]
            if not bcrypt.checkpw(postData['password'].encode(), retrieved_user.password.encode()):
                error.append('Invalid email/password')
                return error
        else:
            error.append('Email is not registered')
            return error

    def logUser(self, postData):
        retrieved_users=User.objects.filter(email=postData['email'])
        if len(retrieved_users) > 0:
            retrieved_user=retrieved_users[0]
            if bcrypt.checkpw(postData['password'].encode(), retrieved_user.password.encode()):
                return retrieved_user
        

class ReviewManager(models.Manager):
    def addBookReviewVal(self, postData):
        error=[]
        if len(postData['title']) < 1:
            error.append('Book title field cannot be blank')
        if len(postData['content']) < 1:
            error.append('Review field cannot be blank')
        return error

    def addBookReview(self, postData, user):
        if len(postData['new_author']) > 0:
            author=Author.objects.create(author_name=postData['new_author'])
        else:
            author=Author.objects.get(id=postData['old_author'])
        book = Book.objects.create(title=postData['title'], author = author.author_name)
        reviewer = User.objects.get(id=user.id)
        review = Review.objects.create(content=postData['content'], rating = postData['rating'], book=book, writer=reviewer)
        return review

    def addReview(self, postData, book, user):
        reviewer=User.objects.get(id=user.id)
        book = Book.objects.get(id=book.id)
        add = Review.objects.create(content=postData['content'], rating = postData['rating'], book=book, writer=reviewer)
        return add

    

class User(models.Model):
    name = models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    objects=UserManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.name)

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    # book_img=models.ImageField(upload_to="book_img", blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Author(models.Model):
    author_name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.author_name)

class Review(models.Model):
    content=models.CharField(max_length=255)
    rating=models.IntegerField()
    writer=models.ForeignKey(User, related_name="users_reviews")
    book=models.ForeignKey(Book, related_name="reviews")
    objects=ReviewManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} {}:{} by {}'.format(self.id, self.book, self.content, self.writer)