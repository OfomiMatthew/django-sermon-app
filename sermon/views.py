from django.shortcuts import render,redirect,get_object_or_404
from .models import * 
from django.contrib.auth.decorators import login_required
from .forms import SermonForm, ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


def home(request):
  searchSermon = request.GET.get('searchSermon')
  if searchSermon:
    sermons = Sermon.objects.filter(title__icontains=searchSermon)
  else:
    sermons = Sermon.objects.all()
  paginator = Paginator(sermons,3)
  page_number = request.GET.get('page',1)
  try:
    sermons = paginator.page(page_number)
  except PageNotAnInteger:
    sermons = paginator.page(1)
  except EmptyPage:
    sermons = paginator.page(paginator.num_pages)
  return render(request,'sermon/home.html',{'sermons':sermons,'searchSermon':searchSermon})
 
    
  
@login_required
def upload_sermon(request):
  if request.method == 'POST':
    form = SermonForm(request.POST, request.FILES)
    if form.is_valid():
      sermon = form.save(commit=False)
      sermon.author = request.user
      sermon.save()
      return redirect('home') 
    else:
      print(form.errors)
  else:
    form = SermonForm()
    
  
  return render(request,'sermon/upload_sermon.html',{'form':form})

@login_required
def list_sermon(request):
  sermon = Sermon.objects.all()
  return render(request,'sermon/list_sermon.html',{'sermons':sermon})

@login_required
def sermon_detail(request,slug):
  sermon = get_object_or_404(Sermon,slug=slug)
  reviews = Review.objects.filter(sermon=sermon)
  return render(request,'sermon/sermon_detail.html',{'sermon':sermon,'reviews':reviews})


@login_required
def create_review(request,id):
  sermon = get_object_or_404(Sermon,pk=id)
  if request.method == 'GET':
    return render(request,'sermon/create_review.html',{'form':ReviewForm(),'sermon':sermon})
  else:
    try:
      form = ReviewForm(request.POST)
      if form.is_valid():
        
        newReview = form.save(commit=False)
        newReview.user = request.user
        newReview.sermon = sermon
        newReview.save()
        return redirect('sermon-detail',slug=newReview.sermon.slug)
      else:
        return render(request,'sermon/create_review.html',{'form': form, 'error': 'Invalid data'})
    except ValueError:
      return render(request,'sermon/create_review.html',{'form':ReviewForm(),'error':'bad data passed'})
  
@login_required
def update_review(request,id):
  review = get_object_or_404(Review,pk=id,user=request.user)
  if request.method == 'GET':
    form = ReviewForm(instance=review)
    return render(request,'sermon/update_review.html',{'review':review,'form':form})
  else:
    try:
      form = ReviewForm(request.POST,instance=review)
      form.save()
      return redirect('sermon-detail',review.sermon.slug)
    except ValueError:
      return render(request,'sermon/update_review.html',{'review':review})
 

@login_required   
def delete_review(request,id):
  review = get_object_or_404(Review,pk=id,user=request.user)
  sermon_slug = review.sermon.slug 
  if request.method == 'POST':
    review.delete()
    messages.info(request,f'Review: {review.text} deleted successfully')
    return redirect('sermon-detail',slug=sermon_slug)
  return render(request,'sermon/delete.html',{'obj':review})
    
