from django.shortcuts import render

def links(request):
    return render(request, 'blog/list.html', context={'name': 'links'})
