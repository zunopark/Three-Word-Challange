from django.shortcuts import render,get_object_or_404, redirect
from main.models import Keyword, Post, Nation
from django.utils import timezone
import datetime
from .forms import PostForm
import random
from django.contrib import messages


current_keyword = ""
current_pk = 0


## 용섭 작업 위해서
def rank(request):
    return render(request, 'rank.html')

def list(request):
    return render(request, 'list.html')

# 아직 미완성
banned_word = ['섹스', 'fuck']

def home(request):
    global current_keyword
    global current_pk

    # 제시어 중에서 표시하고 싶은것 하나만 뽑아야 한다. 
    today_keyword = Keyword.objects.get(is_show=True)
    current_keyword = today_keyword.name
    current_pk = today_keyword.id

    # 랜덤으로 뽑고 싶으면 돌리는 로직
    # while True:
    #     pick = random.choice(keywords)
    #     if current_keyword != pick.name:
    #         current_keyword = pick.name
    #         current_pk = pick.id
    #         break
    
    posts = Post.objects.all().filter(keyword=today_keyword)
    posts = posts.order_by('-num_of_like')

    first = today_keyword.name[0]
    second = today_keyword.name[1]
    third = today_keyword.name[2]

    context = {
        'key' : current_keyword,
        'posts' : posts,
        'first' : first,
        'second' : second,
        'third' : third,
        'keywords' : today_keyword,
    }

    return render(request, 'index.html', context)

def go_create(request):
    global current_keyword
    global current_pk

    first = current_keyword[0]
    second = current_keyword[1]
    third = current_keyword[2]

    obj = Keyword.objects.get(pk=current_pk)
    exp = obj.explanation

    # 애초부터 넣을때 알파벳 순으로 넣어야 한다.
    nation = Nation.objects.all()

    context = {
        'keyword' : current_keyword,
        'first' : first,
        'second' : second,
        'third' : third,
        'exp' : exp,
        'nation' : nation
    }
    return render(request, 'write.html', context)

def check_word(post):
    for elem in banned_word:
        if elem in post.first or elem in post.second or elem in post.third:
            return True
    
    return False


def create_post(request):
    global current_pk
    key = Keyword.objects.get(pk=current_pk)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print('valid')
            post = form.save(commit=False)

            post.first = request.POST.get("first")
            post.second = request.POST.get("second")
            post.third = request.POST.get("third")
            post.nation = request.POST.get("nation")
            post.first_translation = request.POST.get("first_translation")
            post.second_translation = request.POST.get("second_translation")
            post.third_translation = request.POST.get("third_translation")

            # 단어 예외 처리
            # if check_word(post):
            #     messages.add_message(request, messages.WARNING, '올바른 단어를 사용하자!')
            #     return redirect('go_create')

            post.keyword = key
            post.save()
            return redirect('readbylike')
        else:
            print('not valid')
            messages.add_message(request, messages.WARNING, '빈칸을 다 채워주세요!')
            return redirect('go_create')
            
    else:
        form = PostForm()


# 날짜 순으로 제시어 나열해야 한다.
def read_keyword_by_like(request):
    keywords = Keyword.objects.all().order_by('-release_date')

    context = {
        'keywords' : keywords
    }

    return render(request, 'index.html', context)

def raise_heart(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post:
        post.num_of_like += 1
        post.save()
    else:
        return redirect('readbylike')

    return redirect('readbylike')


# 제시어에 따라서 최신 순으로 정렬
def read_posts_by_date(request):
    global current_pk
    global current_keyword
    key = Keyword.objects.get(pk=current_pk)

    today_keyword = Keyword.objects.get(is_show=True)

    posts = Post.objects.all().filter(keyword = key).order_by('-release_date')

    first = key.name[0]
    second = key.name[1]
    third = key.name[2]

    context = {
        'posts':posts,
        'key':current_keyword,
        'first':first,
        'second':second,
        'third':third,
        'keywords' : today_keyword,
    }

    return render(request, 'index.html', context)

# 제시어에 따라서 좋아요 순으로 정렬
def read_posts_by_like(request):
    global current_pk
    global current_keyword
    # 제시어 클릭시 pk 값 넘어옴
    key = Keyword.objects.get(pk=current_pk)

    first = key.name[0]
    second = key.name[1]
    third = key.name[2]

    today_keyword = Keyword.objects.get(is_show=True)


    posts = Post.objects.all().order_by('-num_of_like')
    posts = posts.filter(keyword=key)

    context = {
        'posts':posts,
        'key':current_keyword,
        'first':first,
        'second':second,
        'third':third,
        'keywords' : today_keyword,
    }

    return render(request, 'index.html', context)