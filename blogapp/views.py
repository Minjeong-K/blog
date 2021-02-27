from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator  # 페이지네이션을 위해
from .models import Blog

def home(request):
    blogs = Blog.objects

    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()

    # 블로그 객체 3개를 1페이지로 자르기
    paginator = Paginator(blog_list, 3)
    
    # request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')

    # request된 페이지를 얻어온 뒤 return을 해준다 
    posts = paginator.get_page(page)
    return render(request ,'home.html',{'blogs':blogs,'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

# new.html 띄워주는 함수
def new(request):
    return render(request, "new.html")

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()     # 객체.delete
    return redirect('/blog/'+str(blog.id))
