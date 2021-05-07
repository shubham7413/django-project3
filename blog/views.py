from django.shortcuts import render,HttpResponse
from blog.models import Blog, Contact
import math

# Create your views here.
def home(request):
    # return HttpResponse("this ishome")
    return render(request,'index.html')

def blog(request):
    # return HttpResponse("this is blog")
    no_of_post = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    print(page)

    '''
    1 :  0 - 3
    2 :  3 - 6
    3 :  6 - 9

     1: 0- 0+ no_of_post
     2: no_of_posts to no_of_posts+no_of_posts
     3: no_of_posts+no_of_posts to no_of_posts + no_of_posts+no_of_posts

    (page_no-1)*no_of_posts to page_no*no_of_posts
    '''
    blogs = Blog.objects.all()[(page-1)*no_of_post: page*no_of_post]
    length = len(Blog.objects.all())
    if page > 1:
        prev = page -1
    else:
        prev = None

    if page  < math.ceil(length/no_of_post):
        nxt = page + 1
    else:
        nxt = None

    context = {'blog':blogs,'prev':prev,'nxt':nxt}
    return render(request,'blog.html',context)

def blogpost(request,slug):
    # return HttpResponse(f"You are viewing {slug}")
    blog = Blog.objects.filter().first()
    context = {'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
    # return HttpResponse("this is contact")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
    return render(request,'contact.html')
def search(request):
    # return HttpResponse("this is contact")
    return render(request,'search.html')