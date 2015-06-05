from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from .models import Post, Tag, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from forms import RegisterForm, PostForm, TagForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('publish_time')[:20]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'forum/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/detail.html', {'post': post})

def login_view(request):
    print('wiw')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return index(request)
    else:
        return render(request, 'forum/login.html')

def logout_view(request):
    logout(request)
    return index(request)

def user_register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            #phone = request.POST.get('phone', '')
            errors = []
            print('wow')
            register_form = RegisterForm({'username': username,
                                          'password1': password1,
                                          'password2': password2,
                                          'email': email})
            if not register_form.is_valid():
                errors.extend(register_form.errors.values())
                return render_to_response("forum/userRegister.html", RequestContext(request, {'username': username,
                                                                                              'email': email,
                                                                                              'errors': errors}))
            if password1 != password2:
                errors.append("Different!")
                return render_to_response("forum/userRegister.html", RequestContext(request, {'username': username,
                                                                                              'email': email,
                                                                                              'errors': errors}))

            filter_result = User.objects.filter(username=username)
            if len(filter_result) > 0:
                errors.append("Already exist!")
                return render_to_response("forum/userRegister.html", RequestContext(request, {'username': username,
                                                                                              'email': email,
                                                                                              'errors': errors}))

            user = User()
            user.username = username
            user.set_password(password1)
            user.email = email
            user.save()
            profile = UserProfile()
            profile.user_id = user.id
            #profile.phone = phone
            profile.save()
            new_user = authenticate(username=username,password=password1)
            if new_user is not None:
                login(request, new_user)
                return HttpResponseRedirect("forum:index")
    except Exception, e:
        errors.append(str(e))
        return render_to_response("forum/userRegister.html", RequestContext(request, {'username': username,
                                                                                     'email': email,
                                                                                     'errors': errors}))
    return render_to_response("forum/userRegister.html", RequestContext(request, {}))

def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        tag = TagForm(request.POST)
        if post_form.is_valid() and tag.is_valid():
            cd_tag = tag.cleaned_data
            tag_name = cd_tag['tag_name']
            for tag_list in tag_name.split():
                Tag.objects.get_or_create(tag_name=tag_list.strip())
            title = post_form.cleaned_data['caption']
            user = request.user
            content = post_form.cleaned_data['content']
            post = Post(caption=title, user=user, content=content)
            post.save()
            for tag_list in tag_name.split():
                post.tags.add(Tag.objects.get(tag_name=tag_list.strip()))
                post.save()
            post_id = Post.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/forum/%s' % post.id)
    else:
        post_form =PostForm()
        tag = TagForm(initial={'tag_name': 'others'})
    return render_to_response('forum/add_post.html',
        {'form': post_form, 'tag': tag}, RequestContext(request))