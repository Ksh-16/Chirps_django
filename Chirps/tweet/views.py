from django.shortcuts import render
from .models import Tweet,Like,Comment
from .forms import TweetForm,CommentForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method=="POST":
       form=TweetForm(request.POST,request.FILES)
       if form.is_valid():
           tweet=form.save(commit=False)
           tweet.user=request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        
        if form.is_valid():
            # Check if user wants to remove the photo
            remove_photo = request.POST.get('remove_photo', '0')
            if remove_photo == '1':
                if tweet.photo:
                    tweet.photo.delete()
                tweet.photo = None
            
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request,tweet_id):
        tweet= get_object_or_404(Tweet,pk=tweet_id,user=request.user)
        if request.method=='POST':
            tweet.delete()
            return redirect('tweet_list')
        return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

@login_required
def toggle_like(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    like_obj = Like.objects.filter(user=request.user, tweet=tweet)
    
    if like_obj.exists():
        like_obj.delete()
    else:
        Like.objects.create(user=request.user, tweet=tweet)
    
    return redirect('tweet_list')
 
@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tweet = tweet
            comment.save()
    
    return redirect('tweet_list')
 
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == 'POST':
        comment.delete()
    
    return redirect('tweet_list')
 

def register(request):
     if request.method=='POST':
         form= UserRegistrationForm(request.POST)
         if form.is_valid():
              user=form.save(commit=False)
              user.set_password(form.cleaned_data['password1'])
              user.save()
              login(request,user)
              return redirect('tweet_list')
     else:
          form=UserRegistrationForm()
     
     return render(request,'registration/register.html',{'form':form})

def home_view(request):
     return render(request,'index.html')