from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Users
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import UserDataSerializer
from .models import UserData

class UserDataViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = UserData.objects.all()
 
    # specify serializer to be used
    serializer_class = UserDataSerializer


# Create your views here.


def home(request):
    return render(request,'login.html')


def signup(request):
    return render(request,'register.html')

def textarea(request):
    # userId = request.session.get('userId') 
    # context = {
    #     'userId': userId
    # }
    return render(request,'TextareaUI.html') 
      

# to login user
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = Users.objects.filter(email=email).first()
            if user:
                if user.password == password:
                    print("Login successful")
                    # request.session['userId'] = user.userId
                    return redirect(f"/textarea?userId={user.userId}")
                else:
                    print("Wrong password")
            else:
                print("User does not exist")
        else:
            print("Email or password is empty")
    else:
        print("Request method is not POST")
    return redirect("/")
    

def save_user(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        pswd = request.POST["password"]
        
        new_user = Users(name=name, email=email, password=pswd)
        
        try:    
            new_user.save() 
            return redirect("/textarea")   
        except Exception as e:
            print("Error while saving data: " + str(e))  # Convert 'e' to a string before concatenating
            return redirect("/")
    else:
        print("Something went wrong")
        return redirect("/")


def save_file(request):
    if request.method == "POST":
        pass




