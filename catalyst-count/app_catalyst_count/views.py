from django.shortcuts import render, redirect
from .models import *
from progressbarupload.forms import ProgressBarUploadForm
from chunked_upload.views import ChunkedUploadView
from chunked_upload.models import ChunkedUpload

# Create your views here.
def RegisterView(request):
    return render(request, 'signup.html')

def InsertData(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        flag = request.POST['flag']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']


        user = Users.objects.filter(Email = email)
        if user:
            message = 'User Alraedy Exist'
            return render(request, 'signup.html', {'msg' : message})
        else:
            if password == cpassword:
                newuser = Users.objects.create(UserName = user_name, Email = email, Flag = flag, Password = password)
                message = 'User Successfully Created'
                return render(request, 'login.html',{'msg':message})
            else:
                message = 'Please Check Password'
                return render(request, 'signup.html', {'msg' : message})



def UserLoginForm(request):
    return render(request, 'login.html')

def UserLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Users.objects.get(Email=email)
        if user.Password == password:
            request.session['user_name'] = user.UserName
            print('1-----------------',request.session['user_name'])
            request.session['Email'] = user.Email
            request.session['Password'] = user.Password
            request.session['Flag'] = user.Flag
            return redirect('show_users')
        else:
            message = "Password doest Not Exist"
            return render(request, 'login.html',{'msg' : message})
    else:
        message = "User doest Not Exist"
        return render(request, 'signup.html',{'msg' : message})



def ShowPage(request):
     # Retrieve all users from the database
    users = Users.objects.all()
    return render(request, 'show.html', {'users': users})

class MyChunkedUploadView(ChunkedUploadView):
    model = ChunkedUpload
    field_name = 'file'

    def check_permissions(self, request):
        # Implement any permission checks if needed
        pass

def UploadData(request):
    if request.method == 'POST':
        form = ProgressBarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded file here
            uploaded_file = form.save(commit=False)
            # You can perform additional actions with the file if needed
            uploaded_file.save()
            return render(request, 'upload_data.html', {'form': form, 'uploaded_file': uploaded_file})
    else:
        form = ProgressBarUploadForm()

    return render(request, 'upload_data.html', {'form': form})

def QueryBuilder(request):
    pass

def User(request):
    pass

def Logout(request):
    pass
    


