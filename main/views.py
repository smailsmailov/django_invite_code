from django.shortcuts import render , redirect
from .models import *
from rest_framework.response import Response 
from django.http import JsonResponse
from rest_framework.views import APIView , PermissionDenied 
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

@csrf_exempt
def login_page(request):
    data = {}
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST" : 
        print(request.POST['phone'] , request.POST['code'])
        phone = request.POST['phone'].replace("+" , '').replace('(' , '').replace(')' , '').replace('-' , '')
        _UserUpdate_ = UserUpdate.objects.get(phone = phone)
        print(_UserUpdate_ , request.POST['code'] , _UserUpdate_.code ,  _UserUpdate_.code ==request.POST['code'] )
        if _UserUpdate_.code == request.POST['code'] : 
            user = authenticate(request, id = _UserUpdate_,code = request.POST["code"])
            if user is not None and user.is_active:  
                login(request, user)
    return render(request , 'accounts/login.html' , context=data)


def home_page(request):
    data = {}
    
    return render(request , 'home.html' , context=data)


def profile_page(request):
    data = {}
    
    return render(request , 'home.html' , context=data)

# API USERS_CONNECTED

@login_required()
@csrf_exempt
def GetAllUsersInvites( request):
    if request.method == "GET":
        user = request.user
        print(user)
        # return JsonResponse({})
        _UserUpdateSELF_ = UserUpdate.objects.get(id = user.id)
        _Connected_users_ = Connected_users.objects.filter(conntected_user_extension = _UserUpdateSELF_) 


        all_users ={"users" : [] , "phones":[]}
        for i in _Connected_users_ : 
            userUholder = UserUpdate.objects.get(user= i.user)
            all_users['users'].append(i.user.username)
            all_users['phones'].append(userUholder.phone)
        return JsonResponse(all_users)

@csrf_exempt
def ConnectUserToUser( request):
    if request.method == "POST" :
        invite_code = request.POST['invite_code']
        _UserUpdateSELF_ = UserUpdate.objects.get(user = request.user)
        _UserUpdateTO_ = UserUpdate.objects.filter(invite_code = invite_code)
        _Connected_users_, created = Connected_users.objects.get_or_create(user= _UserUpdateTO_.user , conntected_user_extension = _UserUpdateSELF_)
            # ОТПРАВКА СООБЩЕНИЯ НА ТЕЛЕФОН 
        return Response()

# @api_view(['GET', 'POST'])
@csrf_exempt
def GetCodeAuth( request):
    print(request.method)
    if request.method == "POST" :
        phone = request.POST['phone']
        print(phone)
        if len(phone) == 11 :
            _User_ ,u_created = User.objects.get_or_create(username=phone)
            _UserUpdate_ , created = UserUpdate.objects.get_or_create( user=_User_, phone = phone)
            code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
            if not created :
                _UserUpdate_.code = code 
                _UserUpdate_.save() 
                code = _UserUpdate_.code
            else:
                _UserUpdate_.code = code 
                _UserUpdate_.save()

            # ОТПРАВКА СООБЩЕНИЯ НА ТЕЛЕФОН 
            return JsonResponse({"code" : code })