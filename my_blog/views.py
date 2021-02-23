from django.shortcuts import render

# Create your views here.
def index(request):
    #Home page for my_blog
    return render(request, 'my_blog/index.html')


