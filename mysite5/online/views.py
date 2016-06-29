# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User, Photo, Item
from django.views import generic
from django.http import StreamingHttpResponse


# 表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密  码', widget=forms.PasswordInput())




# 注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 检查用户名是否重复
            num = User.objects.filter(username=username).count()
            if num < 1:
                # 添加到数据库
                User.objects.create(username=username, password=password)
                return HttpResponseRedirect('/online/login/')
                #return HttpResponseRedirect('../login/')
            #页面自动跳转没完成
            else:
                return HttpResponse(u'你的用户名已经存在，请重新填写')

    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))


# 登陆
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)

            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                # 在session中存入 当前用户id
                uid = User.objects.get(username=username)
                req.session['user_id'] = uid.id
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))


# 登陆成功
def index(req):
    username = req.COOKIES.get('username', '')
    userid = req.session['user_id']
    return render_to_response('index.html', {'username': username, 'userid': userid})





# 退出
def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return HttpResponseRedirect('/online/login/')


# 上传图片
# 表单
class PhotoForm(forms.Form):
    title = forms.CharField(label='照片标题', max_length=200)
    image = forms.FileField(label='选择照片')


def upload(req):
    if req.method == "POST":
        pf = PhotoForm(req.POST, req.FILES)
        if pf.is_valid():
            # 获取表单信息
            title = pf.cleaned_data['title']
            image = pf.cleaned_data['image']
            # 写入数据库
            photo = Photo()
            uid = req.session['user_id']
            iid = 1#req.session['item_id']
            photo.title = title
            photo.image = image
            photo.uid = uid
            photo.iid = iid
            photo.save()
            return HttpResponseRedirect('/online/photolist/')
    else:
        pf = PhotoForm()
        return render_to_response('upload.html', {'pf': pf}, context_instance=RequestContext(req))


#下载

def download(request):
    # do something...

    def readfile(fn, buf_size=262144):
        f = open(fn, "rb")
        while True:
            c = f.read(buf_size)
            if c:
                yield c
            else:
                break
        f.close()

    file_name = "photo/5526.jpg"
    #response = HttpResponse(readfile(file_name))
    response = StreamingHttpResponse(readfile(file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    return response

# 删除
# 表单


class PhotoNum(forms.Form):
    num = forms.IntegerField(label='照片编号')


def delete(req):
    if req.method == "POST":
        df = PhotoNum(req.POST, req.FILES)
        if df.is_valid():
            # 获取表单信息
            num = df.cleaned_data['num']
            # 写入数据库
            Photo.objects.get(id=num).delete()
            return HttpResponseRedirect('/online/photolist/')
    else:
        df = PhotoNum()
        return render_to_response('delete.html', {'df': df}, context_instance=RequestContext(req))





# 创建相册


# 相册表单

class ItemForm(forms.Form):
    name = forms.CharField(label='相册名称', max_length=200)
    description = forms.CharField(label='相册描述')


# 创建相册
def newitem(req):
    if req.method == "POST":
        ni = ItemForm(req.POST)
        if ni.is_valid():
            # 获取表单信息
            name = ni.cleaned_data['name']
            description = ni.cleaned_data['description']
            # 写入数据库
            item = Item()
            uid = req.session['user_id']
            item.name = name
            item.description = description
            item.uid = uid
            item.save()
            return HttpResponseRedirect('/online/index/')
    else:
        ni = ItemForm()
        return render_to_response('home.html', {'ni': ni}, context_instance=RequestContext(req))


# 相册列表
def itemlist(req):
    uid = req.session['user_id']
    items = Item.objects.filter(uid='%d' % uid)
    return render_to_response('itemlist.html', {'items': items}, context_instance=RequestContext(req))


# 照片列表
def photolist(req):
    iid = 1
    photos = Photo.objects.filter(iid='%d' % iid)
    return render_to_response('photolist.html', {'photos': photos}, context_instance=RequestContext(req))







