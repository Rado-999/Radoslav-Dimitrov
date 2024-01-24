from django.shortcuts import render


def homepage(request):
    return render(request, 'welcome_page.html')
