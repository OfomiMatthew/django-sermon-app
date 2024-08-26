from django.urls import path 
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('',views.home,name='home'),
    path('upload-sermon',views.upload_sermon,name='upload-sermon'),
    path('list-sermon',views.list_sermon,name='list-sermon'),
    path('sermon/<slug:slug>/',views.sermon_detail,name='sermon-detail'),
    path('<int:id>/create/',views.create_review,name='create-review'),
    path('<int:id>/update/',views.update_review,name='update-review'),
    path('<int:id>/delete/',views.delete_review,name='delete-review'),
]

handler404 = 'sermon.urls.custom_page_not_found_view'