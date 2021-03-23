from django.shortcuts import render,HttpResponse,redirect
from .models import Posts,Usercomment
from django.contrib import messages
from blog.templatetags import extra

# Create your views here.
def bloghome(request):
    mypost=Posts.objects.all()
    context={'mypost':mypost}
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post=Posts.objects.filter(slug=slug).first()
    comment=Usercomment.objects.filter(post=post, parent=None)
    replies=Usercomment.objects.filter(post=post).exclude(parent=None)
    replydict={}
    for reply in replies:
        if reply.parent.sno not in replydict:
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    context={'post':post,'comment':comment,'user':request.user,'replydict':replydict}
    return render(request,'blog/blogpost.html',context)
def usercomment(request):
    if request.method=='POST':
        postsno=request.POST.get('postsno')
        print(postsno)
        post=Posts.objects.get(sno=postsno)
        comm=request.POST.get("comments")
        user=request.user
        parentsno=request.POST.get("parentsno")
        if parentsno == "":
            comments=Usercomment(comment=comm,user=user,post=post)
            messages.success(request,'your commented successfully')
        else:
            parent=Usercomment.objects.get(sno=parentsno)
            comments=Usercomment(comment=comm,user=user,post=post,parent=parent)
            messages.success(request,'your reply successfully')
        comments.save()   
    return redirect(f"/blog/{post.slug}")