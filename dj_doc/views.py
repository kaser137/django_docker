from django.shortcuts import render, loader, redirect, HttpResponse


def index(requset):
    return render(requset,'index.html')