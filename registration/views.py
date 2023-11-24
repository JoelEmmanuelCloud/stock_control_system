from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import userCreationForm

def register(response):
    form = userCreationForm()
    return render(response, "register/register.html", {"form": form})

