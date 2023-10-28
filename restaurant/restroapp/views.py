from django.shortcuts import render, redirect,HttpResponse
from .models import bookmodel, restroModel,apimodel
import json
import requests
# Create your views here.

# def getWeather(city):
def getWeather(request):   
    city='' 
    result=''
    appid="185a5b60b5b86a369f84a06359abb723"
    if request.GET:
        city=request.GET['city']
    url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
    # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b&units=metric"
    response=requests.get(url)
    result=json.loads(response.text)
    jsondata=result
    ob=apimodel()
    ob.city=city
    ob.jsondata=jsondata
    ob.save()
    return render(request,"getcity.html",{"city":city,"result":result})
# return response.text
# cities="Delhi,Lucknow,Varanasi,Jaipur,jaunpur,Mumbai"
# cities=cities.split(",")
# for city in cities:
#     data=getWeather(city)
#     jsondata=data
#     # print(city,"\n",data,",",len(data),"\n")
#     print(len(data),"\n")

#     ob=apimodel()
#     ob.city=city
#     ob.jsondata=jsondata
#     ob.save()

def getwdata(request):
    city=''
    data=''
    result=''
    status=''
    if request.GET:
        city=request.GET['city']
        data=apimodel.objects.filter(city=city)
        if len(data)<=0:
            result='not found'
        else:
            data=data[0]
            status=data
            result='success'
    return render (request,'find.html',{'result':result,'city':city,'status':status})
    



def people(request):
    url=request.GET["peopleno"]
    response=requests.get(url)
    code=response.status_code
    print(code)
    if code !=200:
            status="error"
            print("error")
            return HttpResponse("Error")
    else:
         result=json.loads(response.text)
         return render(request,"people.html",{"result":result})
        
    return HttpResponse(url)



def index(request):
    return render(request, "bootstrap.html")


def registration(request):
    username = ""
    name = ""
    password = ""
    cnfirmpsswrd = ""
    submit = ""
    result = ""
    if request.POST:
        try:
            username = request.POST["username"]
            name = request.POST["name"]
            password = request.POST["password"]
            cnfirmpsswrd = request.POST["cnfirmpsswrd"]
            if password == cnfirmpsswrd:
                db = restroModel()
                db.username = username
                db.name = name
                db.password = password
                db.save()
                result = "Registration done successfully"
            else:
                result = "Incorrect Password"

        except:
            result = "User Already Exist"

    return render(request, "register.html", {"username": username, "name": name, "pw": password,
                                             "cpw": cnfirmpsswrd, "rslt": result, "submit": submit})


def dologin(request):
    username = ""
    password = ""
    result = ""
    data = ""
    if request.POST:

        username = request.POST['username']
        password = request.POST['password']
        data = restroModel.objects.filter(
            username=username).filter(password=password)
        if len(data) <= 0:
            result = "Incorrect Username or Password"
            return render(request, "dologin.html", {"result": result})
        else:
            data = data[0]
            username = data.username
            # print(username)
            request.session['username'] = username
            return redirect('/home')

    return render(request, "dologin.html", {"result": result, "username": username, "password": password})


def home(request):
    currentuser = request.session.get("username")
    if currentuser is None:
        return redirect('/login')
    else:
        # context = {'currentuser': currentuser}
        # return render(request, "home.html", context)

        return render(request, "home.html", {'currentuser': currentuser})

        # return HttpResponse("Welcome  "+ currentuser)


def logout(request):
    session = request.session
    session.pop("username")
    return redirect('/login')




def create(request):
    category=""
    author=""
    name=""
    result=""
    if request.GET:
        category=request.GET["category"]
        author=request.GET["author"]
        name=request.GET["name"]
        try:
          ob = bookmodel()
          ob.category=category
          ob.author=author
          ob.name=name
          ob.save() 
          result="Successfull"
        except:
           result="Not enter"
    return render (request,"book.html",{"category":category,"author":author,"name":name,"result":result})       

def search(request):
    category=""
    data=""
    result=""
    if request.GET:
        category=request.GET['category']
        data=bookmodel.objects.filter(category=category)
        if len(data)<=0:
            result="Not found "
        else:
            
            result="Found " + str(len(data)) + " records."
          #   data=data[0]
          #   name=data.name
          #   author=data.author
    return render (request,"search.html",{"category":category,"result":result,"data":data})

def delete(request):
    book_data=''
    id_value=''
    result=''
    if request.GET:
        try:
            id_value=int(request.GET['id'])
            book_data=bookmodel.objects.filter(id=id_value)
            if len(book_data)<=0:
                result="not found"
            else:
             book_data=book_data[0]
             book_data.delete()
             result=" remove " 
        except: 
            result="invalid id"
        
           
    return render (request,"delete.html",{"id":id_value,"result":result,"data":book_data})

def update(request):
    name=''
    author=''
    # category=''
    result=''
    if request.GET:
        name=request.GET['name']
        author=request.GET['author']
        if id==id:
          ob = bookmodel()
          ob.author=author
          ob.name=name
          ob.save() 
          result="save"
        else:
            result="not save"
    return render (request,"update.html",{"name":name,"author":author,"result":result})        





def weather(request):
    appid="185a5b60b5b86a369f84a06359abb723"
    city="Varanasi"
    if request.GET:
       city=request.GET["city"]
    #    city=input("Enter city\n")
    params={'aapid':appid,"q":city,"units":"metric"}
    url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
    # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b&units=metric"
    response=requests.get(url,params)
    code=response.status_code
    print(code)
    
    # 200 means success
    # status code 404 not found 
    # sttus code 401 is not authorized
    # print(response.text)

    if code != 200:
            print("error")
            return render(request,"weather.html",{"result":"error","city":city,"img":"error"})
    else:
            result=json.loads(response.text)
            # result=response.text
            # print(jsondata)

    return render(request,"weather.html",{"result":result,"city":city,"img":result["weather"][0]["icon"]})



def swapi(request):
    filmno='1'
    # actor="actor"
    result=''
    status=''
    # people=''
    if request.GET:
        filmno= request.GET['filmno']
    try:
        url="https://swapi.dev/api/films/"+filmno
        # url="https://swapi.dev/api/people/"
        response=requests.get(url)
        code=response.status_code
        print(code)
        if code !=200:
            status="error"
            print("error")
            return render(request,"swapi.html",{"result":"","status":status})
        else:
            result=json.loads(response.text)
            status="success"
    except:
            status="error"
    return render(request,"swapi.html",{"filmno":filmno,"people":result["characters"],"result":result,"status":status})
        # return HttpResponse(response.text)


def movie(request):
    result=""
    url="https://gist.githubusercontent.com/AzadIdrisi88/fd0cd6d617c599c183b23e2ef7378b10/raw/2b76d7d01c7ae03cc6cfcd965c9bb49ef3935ac0/mysecondgist"
    response=requests.get(url)
    code=response.status_code
    print(code)
    if code !=200:
            status="error"
            print("error")
            return HttpResponse("Error")
    else:
         result=json.loads(response.text)
         status=''
    return render(request,"film.html",{"result":result,"status":status})        