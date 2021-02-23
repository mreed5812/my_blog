from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    #Home page for my_blog
    return render(request, 'my_blog/index.html')

def topics(request):
    #Show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_blog/topics.html', context)
