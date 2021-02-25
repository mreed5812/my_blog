#Define URL patterns for my_blog

from django.urls import path

from . import views

app_name = 'my_blog'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #Page that shows all topics
    path('topics/', views.topics, name='topics'),

    #Detail page for a topic
    path('topics/<int:topic_id>', views.topic, name='topic'),

    # Page for adding a topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    

]