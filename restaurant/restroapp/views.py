from django.shortcuts import render ,HttpResponse ,redirect
from.models import restroModel
# Create your views here.
def index(request):
    return render(request,"bootstrap.html")

def registration(request):
        username=""
        name=""
        password=""
        cnfirmpsswrd=""
        submit=""
        result=""
        if request.POST:
            try:
              username=request.POST["username"]
              name=request.POST["name"]
              password=request.POST["password"]
              cnfirmpsswrd=request.POST["cnfirmpsswrd"]
              if password == cnfirmpsswrd:
                    db=restroModel()
                    db.username=username
                    db.name=name
                    db.password=password
                    db.save()
                    result="Registration done successfully"
              else:
                   result="Incorrect Password"


            except:
                 result="User Already Exist"

        return render(request,"register.html",{"username":username,"name":name,"pw":password,
                        "cpw":cnfirmpsswrd,"rslt":result, "submit":submit})
              
       
def dologin(request):
     username=""
     password=""
     result=""
     data=""
     if request.POST:
      
        username=request.POST['username']
        password=request.POST['password']
        data=restroModel.objects.filter(username=username).filter(password=password)
        if len(data)<=0:
            result="Incorrect Username or Password"
            return render (request,"dologin.html",{"result":result})
        else:
            data=data[0]
            username=data.username
            # print(username)
            request.session['username']=username
            return  redirect ('/home',)
          
     return render(request,"dologin.html",{"result":result,"username":username,"password":password })

def home(request):
     currentuser=request.session.get("username")
     if currentuser is None:
          return redirect('/login')
     else:
          # context = {'currentuser': currentuser} 
          # return render(request, "home.html", context)
         
          return render(request,"home.html",{'currentuser': currentuser})
     
          # return HttpResponse("Welcome  "+ currentuser)
          
