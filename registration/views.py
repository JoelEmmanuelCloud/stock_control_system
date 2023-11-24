from django.shortcuts import render

def register(response):
    return render(response, "register/register.html", {})