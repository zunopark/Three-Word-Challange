from django.shortcuts import render,get_object_or_404, redirect
from main.models import Keyword, Post, Nation
from django.utils import timezone
import datetime
from .forms import PostForm
import random
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

current_keyword = ""
current_pk = 0

@csrf_exempt
def update_bool(request, pk):
    message = 'update successful'
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if post.is_trans == True:
            post.is_trans = False
        else:
            post.is_trans = True
        post.save()
    return HttpResponse(message)

def translate(request, pk):
    post = get_object_or_404(Post, id=pk)
    
    tr1 = post.trans_1
    tr2 = post.trans_2
    tr3 = post.trans_3

    is_clicked = post.is_trans

    context = {
        'tr1' : tr1,
        'tr2' : tr2,
        'tr3' : tr3,
        'is_clicked':is_clicked
    }

    return JsonResponse(context)

def rank(request):
    update_rank()
    all_nation = Nation.objects.all().order_by('-sum_of_like')

    length = [i for i in range(1, len(all_nation)+1)]

    context = {
        'nations' : all_nation,
        'length' : length
    }

    return render(request, 'rank.html', context)

def update_rank():
    all_posts = Post.objects.all()

    all_nation = Nation.objects.all()

    for elem in all_nation:
        _sum = 0
        for posts in all_posts:
            if posts.nation_name == elem.name:
                _sum += posts.num_of_like
        
        total_post = Post.objects.all().filter(nation=elem)

        elem.total_post = len(total_post)
        elem.sum_of_like = _sum
        elem.save()


def list(request):
    global current_keyword
    today_keyword = Keyword.objects.get(name=current_keyword)
    today_keyword.is_show = False

    keywords = Keyword.objects.all().order_by('-release_date')

    update_list_rank()

    context = {
        'keywords' : keywords
    }

    return render(request, 'list.html', context)

def update_list_rank():
    all_keywords = Keyword.objects.all()
    
    for elem in all_keywords:
        posts = Post.objects.all().filter(keyword=elem).order_by('-num_of_like')[:3]
        p = Post.objects.all().filter(keyword=elem)
        elem.sum_of_like = len(p)
        elem.first_nation = posts[0].nation
        elem.second_nation = posts[1].nation
        elem.third_nation = posts[2].nation
        elem.save()


def other_prompt(request, pk):
    global current_keyword
    global current_pk

    today_keyword = Keyword.objects.get(pk=pk)
    today_keyword.is_show = True

    current_keyword = today_keyword.name
    current_pk = today_keyword.id

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

# 아직 미완성
banned_word = ['섹스', 'fuck', '색스', 'Fuck', '시발', '씨발', 'Sex', 'SEX']

def home(request):
    global current_keyword
    global current_pk

    # 제시어 중에서 is_show == True인 것 하나를 반환
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
        'nation' : nation,
    }

    return render(request, 'write.html', context)

def check_word(post):
    for elem in banned_word:
        if elem in post.first or elem in post.second or elem in post.third or elem in post.nickname:
            return True
    
    return False


def create_post(request):
    global current_pk
    key = Keyword.objects.get(pk=current_pk)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.first = request.POST.get("first")
            post.second = request.POST.get("second")
            post.third = request.POST.get("third")
            post.nation_name = request.POST.get("nation")
            post.nickname = request.POST.get("nickname")

            try:
                n = Nation.objects.get(name=post.nation_name)
                post.nation = n
            except:
                messages.add_message(request, messages.WARNING, 'Please Fill in all Required Fields')
                return redirect('go_create')

            #단어 예외 처리
            if check_word(post):
                messages.add_message(request, messages.WARNING, 'Please do not use the bad words!')
                return redirect('go_create')

            post.keyword = key
            post.save()
            return redirect('readbylike')
        else:
            print('not valid')
            messages.add_message(request, messages.WARNING, 'Please Fill in all Required Fields!')
            return redirect('go_create')
            
    else:
        form = PostForm()


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

    return render(request, 'recent.html', context)

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