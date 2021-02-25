from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    #Home page for my_blog
    return render(request, 'my_blog/index.html')

def topics(request):
    #Show all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_blog/topics.html', context)

def topic(request, topic_id):
    #Detail page for a topic
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'my_blog/topic.html', context)

def new_topic(request):
    #Add new topic
    if request.method != 'POST':
        #No data submitted, create a blank form.
        form = TopicForm()
    else:
        #POST data submitted
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_blog:topics')
    
    #Display a blank form
    context = {'form': form}
    return render(request, 'my_blog/new_topic.html', context)

def new_entry(request, topic_id):
    #Add new entry for a topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted
        form = EntryForm()
    else:
        # POST data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('my_blog:topic', topic_id=topic_id)
        
    #Display blank form
    context = {'topic' : topic, 'form': form}
    return render(request, 'my_blog/new_entry.html', context)

def edit_entry(request, entry_id):
    #Edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Initial request, pre-fill with current entry.
        form = EntryForm(instance=entry)
    else:
        #Post data submitted
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_blog:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'my_blog/edit_entry.html', context)