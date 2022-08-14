from django.shortcuts import render
from trains.models import train
from django.contrib import messages
from trains.models import user
from django.core.mail import send_mail
from trains.models import train_stations
# Create your views here.
def index(request):
    return render(request,'login.html')
def home(request):
    un = request.session.get('un')
    if un is None:
        messages.error(request, 'ERROR: Please login first')
        return render(request, 'login.html')
    else:
        #request.session['un'] = un
        return render(request, 'home.html', {'un':un})
def addTrain(request):

    if request.method == "GET":
        un = request.session.get('un')
        if un is None:
             messages.error(request, 'ERROR: Please login first')
             return render(request, 'login.html')
        elif un=='admin':
            request.session['un'] = un
            return render(request,'addTrain.html')
        else:
            t_list = train_stations.objects.select_related().all()
            # request.session['un'] = un
            messages.error(request, 'ERROR: Only Administrator has the permission')
            return render(request, 'fetch.html', {'t_list': t_list})
    if request.method=='POST':
        tid = request.POST['train_id']
        try:
            train_d = train.objects.get(train_id=tid) # this will throw an error when tid is not there in the database
        except: # train doesnt exists in the database. So create new train details
            t = train()
            t.train_id = tid
            t.start_station = request.POST['start_station']
            t.end_station = request.POST['end_station']
            t.dept_time = request.POST['dept_time']
            t.arr_time = request.POST['arr_time']
            t.total_seats = request.POST['total_seats']
            t.train_name = request.POST['train_name']
            t.save()
            train_d = train.objects.get(train_id=tid)
            ts = train_stations()
            ts.train = train_d
            ts.station_1 = request.POST['station1']
            ts.station_2 = request.POST['station2']
            ts.save()
            messages.success(request, 'SUCCESS: Train added successfully.')
        else:  # train exists with that ID. So should not create a new one.
            messages.error(request, 'ERROR: TrainID already exists.')
        t_list = train_stations.objects.select_related().all()
        un = request.session.get('un')
        return render(request, 'fetch.html', {'t_list': t_list, 'un': un})
        #return render(request, 'fetch.html', {'t_list': t_list})
def fetch(request):
    un = request.session.get('un')
    if  un is None:
        messages.error(request, 'ERROR: Please login first')
        return render(request, 'login.html')
    else:
        t_list = train_stations.objects.select_related().all()
        return  render(request,'fetch.html',{'t_list':t_list, 'un':un})
def update(request):
    un = request.session.get('un')
    if  un is None:
        messages.error(request, 'ERROR: Please login first')
        return render(request, 'login.html')
    elif un == 'admin':
        try:
            tid = request.POST['tid']
        except:
            t_list = train_stations.objects.select_related().all()
            # request.session['un'] = un
            messages.error(request, 'ERROR: First select the train then update the details')
            return render(request, 'fetch.html', {'t_list': t_list, 'un':un})
        else:
            train_details = train_stations.objects.select_related().get(train_id=tid)
            #request.session['un'] = un
            return render(request,'update.html',{'train_details':train_details})
    else:
        t_list = train_stations.objects.select_related().all()
        #request.session['un'] = un
        messages.error(request, 'ERROR: Only Administrator has the permission')
        return render(request, 'fetch.html', {'t_list': t_list})
def delete(request):
    un = request.session.get('un')
    if  un is None:
        messages.error(request, 'ERROR: Please login first')
        return render(request, 'login.html')
    elif un == 'admin':
        try:
            tid = request.POST['tid']
        except:
            t_list = train_stations.objects.select_related().all()
            # request.session['un'] = un
            messages.error(request, 'ERROR: First select the train then delete the records')
            return render(request, 'fetch.html', {'t_list': t_list, 'un':un})
        else:
            train_details = train.objects.get(train_id = tid)
            train_details.delete()
            t_list = train_stations.objects.select_related().all()
            messages.success(request,'SUCCESS: Record Deleted Successfully.')
            return render(request, 'fetch.html', {'t_list': t_list, 'un':un})
    else:
        t_list = train_stations.objects.select_related().all()
        #request.session['un'] = un
        messages.error(request, 'ERROR: Only Administrator has the permission')
        return render(request, 'fetch.html', {'t_list': t_list})
def modify(request):
    un = request.session.get('un')
    if  un is None:
        messages.error(request, 'ERROR: Please login first')
        return render(request, 'login.html')
    elif un == 'admin':
        t = train()
        t.train_id = request.POST['train_id']
        t.start_station = request.POST['start_station']
        t.end_station = request.POST['end_station']
        t.dept_time = request.POST['dept_time']
        t.arr_time = request.POST['arr_time']
        t.total_seats = request.POST['total_seats']
        t.train_name = request.POST['train_name']
        t.save()

        train_d = train.objects.get(train_id=request.POST['train_id'])
        ts = train_stations()
        ts.id = request.POST['id']
        ts.train = train_d
        ts.station_1 = request.POST['station1']
        ts.station_2 = request.POST['station2']
        ts.save()
        messages.success(request, 'SUCCESS: Record Has been Modified')
        un = request.session.get('un')
        t_list = train_stations.objects.select_related().all()
        return render(request, 'fetch.html', {'t_list': t_list, 'un': un})
    else:
        t_list = train_stations.objects.select_related().all()
        #request.session['un'] = un
        messages.error(request, 'ERROR: Only Administrator has the permission')
        return render(request, 'fetch.html', {'t_list': t_list})
def contactus(request):
    un = request.session.get('un')
    return render(request, 'contactus.html', {'un': un})
def login(request):
    username = request.POST['user_name']
    user_pwd = request.POST['password']
    try :
        user_details = user.objects.get(user_name=username)
    except:
        messages.error(request,"ERROR: User doesn't exists")
        return render(request, 'login.html')
    else:
        if user_details.user_password == user_pwd:
            request.session['un']=username
            return render(request, 'home.html',{'un':username})
        else:
            messages.error(request, 'ERROR: Please enter correct password')
            return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method=='POST':
        username = request.POST['user_name']
        if len(username)==0:
            messages.error(request, "ERROR: Please enter valid user name")
            return render(request, 'register.html')
        else:
            try:
                user_details = user.objects.get(user_name=username) # this will throw an error when user is not there in the database
            except: # if user is not there in the DB, we can create a new user.
                user_pwd1= request.POST['password1']
                user_pwd2 = request.POST['password2']
                if user_pwd1==user_pwd2:
                    u = user()
                    u.user_name = username
                    u.user_password = user_pwd1
                    u.save()   #creating the new user
                    messages.success(request, 'SUCCESS: User has been registered successfully.')
                    return render(request, 'login.html')   # redirecting to login to login with new username / pwd
                else:
                    messages.error(request, "ERROR: Password doesn't match")
                    return render(request, 'register.html')
            else:  # user already exists with that username. So should not create a new user with the same name
                messages.error(request, 'ERROR: User already exists.')
                return render(request, 'register.html')
def logout(request):
    request.session['un']=None
    return render( request,'login.html')
def mail(request):
    msg = request.POST['message']
    username = request.POST['name']
    useremail = request.POST['email']
    userphone = request.POST['phone']
    send_mail(
        'Enquiry - from ' + username,
         msg + ' Phone: ' + userphone,
         useremail,
        ['rupalimulje58@gmail.com'],
        fail_silently=False,
    )
    messages.success(request, 'SUCCESS: Mail has been sent successfully.')
    un = request.session.get('un')
    return render(request, 'contactus.html', {'un': un})
def enquire(request):
    un = request.session.get('un')
    if request.method == "GET":
        if un is None:
             messages.error(request, 'ERROR: Please login first')
             return render(request, 'login.html')
        else:
            return render(request, 'enquire.html')
    if request.method=='POST':
        try:
            search = request.POST['search']
        except:
            messages.error(request, 'ERROR: Enter any one of the details')
            return render(request, 'enquire.html')
        else:
            if search == 't_name':
                t_name = request.POST['train_name']
                if t_name:
                    try:
                       t = train.objects.get(train_name=t_name)
                       t_list = train_stations.objects.select_related().get(train_id=t.train_id)
                    except:
                        messages.info(request, 'INFO: This train name does not exists in our database')
                        return render(request, 'enquire.html')
                else:
                    messages.error(request, 'ERROR: Enter the train name and click submit')
                    return render(request, 'enquire.html')
            elif search == 't_start':
                start_station = request.POST['start_station']
                if start_station:
                    try:
                        t = train.objects.get(start_station=start_station)
                        t_list = train_stations.objects.select_related().get(train_id=t.train_id)
                    except:
                        messages.info(request, 'INFO: This station name does not exists in our database')
                        return render(request, 'enquire.html')
                else:
                    messages.error(request, 'ERROR: Enter the start station name and click submit')
                    return render(request, 'enquire.html')
            elif search == 't_end':
               end_station = request.POST['end_station']
               if end_station:
                   try:
                       t = train.objects.get(end_station=end_station)
                       t_list = train_stations.objects.select_related().get(train_id=t.train_id)
                   except:
                       messages.info(request, 'INFO: This station name does not exists in our database')
                       return render(request, 'enquire.html')
               else:
                    messages.error(request, 'ERROR: Enter the end station name and click submit')
                    return render(request, 'enquire.html')
            return render(request, 'fetch.html', {'t_list': [t_list], 'un': un})



