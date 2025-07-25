import os
import time

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *


def index(request):
    obj = itemdata.objects.filter()
    data = obj
    return render(request, 'index.html', {'data': data})


def about(request):
    return render(request, 'about.html')


def price(request):
    return render(request, 'price.html')





def bread(request):
    return render(request, 'bread.html')


def featured(request):
    return render(request, 'featured.html')




def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['T1']
        password = request.POST['T2']
        obj = logindata.objects.get(email=email, password=password)
        usertype = obj.usertype
        request.session['usertype'] = usertype
        request.session['email'] = email
        if usertype == 'admin':
            return HttpResponseRedirect('/Home/')
        elif usertype == 'user':
            return HttpResponseRedirect('/Product/')
        else:
            return render(request, 'login.html', {'msg': "Faild Login"})
    else:
        return render(request, 'login.html')


def logout(request):
    try:
        del request.session['email']
        del request.session['usertype']
    except:
        pass
    return HttpResponseRedirect('/login/')


def AdminHome(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            obj = admindata.objects.filter(email=email)
            obj1 = photodata.objects.filter(email=email)
            data1 = obj1
            data = obj

            return render(request, 'AdminHome.html', {"data": data, "data1": data1})
        else:
            return HttpResponseRedirect('/AuthError/')
    return render(request, 'login.html', {'msg': "Faild Login"})


def UserHome(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            obj = userdata.objects.filter(email=email)
            obj1 = photodata.objects.filter(email=email)
            obj4 = userdata.objects.filter(email=email)
            obj3 = cartdata.objects.filter(email=email)
            data = obj
            data1 = obj1
            datas = obj4
            data3 = obj3
            i = 0
            for d in data3:
                l = d.item_name
                i = i + 1
            print(i)

            return render(request, 'UserHome.html', {"data": data, "data1": data1, 'datas': datas, 'count': i})
        else:
            return HttpResponseRedirect('/AuthError/')
    return render(request, 'login.html', {'msg': "Faild Login"})


def Product(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            obj2 = itemdata.objects.filter()
            obj = userdata.objects.filter(email=email)
            obj3 = cartdata.objects.filter(email=email)
            data2 = obj2
            data3 = obj3
            i = 0
            for d in data3:
                l = d.item_name
                i = i + 1
            print(i)

            datas = obj
            return render(request, 'Product.html', {"datas": datas, "data2": data2, "data3": data3, 'count': i})
        else:
            return HttpResponseRedirect('/AuthError/')
    return render(request, 'login.html', {'msg': "Faild Login"})


def AuthError(request):
    return render(request, 'AuthError.html')


def AdminReg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == "POST":
                obj = admindata()
                obj1 = logindata()

                a = request.POST['T1']  # name
                b = request.POST['T2']  # address
                c = request.POST['T3']  # contact
                d = request.POST['T4']  # email

                e = request.POST['T5']

                obj.name = a
                obj.address = b
                obj.contact = c
                obj.email = d

                obj1.email = d
                obj1.password = e
                obj1.usertype = "admin"

                obj.save()
                obj1.save()
                return render(request, 'AdminReg.html', {'msg': "success"})
            else:
                return render(request, 'AdminReg.html')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def ShowAdmins(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            data = admindata.objects.all()
            return render(request, 'ShowAdmins.html', {'data': data})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('AuthError/')

def check_email(e1):
    obj=logindata.objects.filter(email=e1)
    if obj:
        return True
    else:
        return False
def UserReg(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                obj = userdata()
                obj1 = logindata()
                a = request.POST['T1']  # name
                b = request.POST['T2']  # address
                c = request.POST['T3']  # contact
                d = request.POST['T4']  # email
                e = request.POST['T5']  # password
                data=check_email(d)
                print(data)
                if data:
                    msg = "User already registered"
                else:
                    obj.name = a
                    obj.address = b
                    obj.contact = c
                    obj.email = d
                    obj.balance = 0
                    obj1.email = d
                    obj1.password = e
                    obj1.usertype = "user"
                    obj.save()
                    obj1.save()
                    msg="success"
                return render(request, 'UserReg.html', {'msg':msg})
            else:
                return render(request, 'UserReg.html')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')




def ShowUser(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            data = userdata.objects.all()
            return render(request, 'ShowUser.html', {'data': data})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def EditUser(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                e1 = request.POST['H1']
                data = userdata.objects.filter(email=e1)
                return render(request, 'EditUser.html', {'data': data})
            else:
                return HttpResponseRedirect("../Autherror/")
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def EditUser1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                a = request.POST['T1']  # name
                b = request.POST['T2']  # address
                c = request.POST['T3']  # contact
                email = request.POST['T4']  # email

                obj = userdata.objects.get(email=email)

                obj.name = a
                obj.address = b
                obj.contact = c

                obj.save()

                return render(request, 'EditUser1.html', {'data': "success"})
            else:
                return HttpResponseRedirect("../AuthError/")
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def DeleteUser(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                e1 = request.POST['H1']
                data = userdata.objects.filter(email=e1)
                return render(request, 'DeleteUser.html', {'data': data})
            else:
                return HttpResponseRedirect("../AuthError/")
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def DeleteUser1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                e1 = request.POST['T4']
                obj = userdata.objects.get(email=e1)
                obj.delete()
                return render(request, 'DeleteUser1.html', {'data': "Delete Success"})
            else:
                return HttpResponseRedirect("../AuthError/")
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def AdminPhotoUpload(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                return render(request, 'AdminPhotoUpload.html', {'email': email})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def AdminPhotoUpload1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                if request.method == 'POST':
                    upload_file = request.FILES['F1']
                    print(upload_file)
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    fs = FileSystemStorage()
                    fs.save(filename, upload_file)
                    obj = photodata()
                    obj.email = email
                    obj.photo = filename
                    obj.save()
                    return render(request, 'AdminPhotoUpload.html', {'msg': "Photo Upload success"})
                else:
                    return HttpResponseRedirect('/AuthError/')
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def UserPhotoUpload(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'user':
                return render(request, 'UserPhotoUpload.html', {'email': email})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def UserPhotoUpload1(request):
    if request.method == "POST":
        print(request.method)
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'user':
                print(usertype)
                if request.method == 'POST':
                    upload_file = request.FILES['F1']
                    print(upload_file)
                    path = os.path.basename(upload_file.name)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    fs = FileSystemStorage()
                    fs.save(filename, upload_file)
                    obj = photodata()
                    obj.email = email
                    obj.photo = filename
                    obj.save()
                    return render(request, 'UserPhotoUpload.html', {'msg': "Photo Upload success"})
                else:
                    return HttpResponseRedirect('/AuthError/')
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def EditAdminProfile(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                obj = admindata.objects.filter(email=email)
                data = obj

                return render(request, 'EditAdminProfile.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def EditAdminProfile1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                a = request.POST['T1']  # name
                b = request.POST['T2']  # address
                c = request.POST['T3']  # contact
                email = request.POST['T4']  # email

                obj = admindata.objects.get(email=email)

                obj.name = a
                obj.address = b
                obj.contact = c

                obj.save()

                return render(request, 'EditAdminProfile1.html', {'msg': "Saved Succes"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def EditUserProfile(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'user':
                obj = userdata.objects.filter(email=email)
                data = obj
                return render(request, 'EditUserProfile.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/login/')


def EditUserProfile1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'user':
                a = request.POST['T1']  # name
                b = request.POST['T2']  # address
                c = request.POST['T3']  # contact
                email = request.POST['T4']  # email

                obj = userdata.objects.get(email=email)

                obj.name = a
                obj.address = b
                obj.contact = c

                obj.save()

                return render(request, 'EditUserProfile1.html', {'msg': "Saved Succes"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ChangeAdminPassword(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                email = request.POST['T1']
                return render(request, 'ChangeAdminPassword.html', {'email': email})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ChangeAdminPassword1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            print(email)
            if usertype == 'admin':
                old_password = request.POST['T1']
                new_password = request.POST['T2']

                obj = logindata.objects.get(email=email)
                if obj.password == old_password:
                    obj.password = new_password
                    print(obj.password)
                    obj.save()
                    return render(request, 'ChangeAdminPassword1.html', {'msg': "Saved Succes"})
                else:
                    return render(request, 'ChangeAdminPassword.html', {'msg': "Old Password Incorrect"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ChangeUserPassword(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'user':
                email = request.POST['T1']
                return render(request, 'ChangeUserPassword.html', {'email': email})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ChangeUserPassword1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            print(email)
            if usertype == 'user':
                old_password = request.POST['T1']
                new_password = request.POST['T2']

                obj = logindata.objects.get(email=email)
                if obj.password == old_password:
                    obj.password = new_password
                    print(obj.password)
                    obj.save()
                    return render(request, 'ChangeUserPassword1.html', {'msg': "Saved Succes"})
                else:
                    return render(request, 'ChangeUserPassword.html', {'msg': "Old Password Incorrect"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AddBalance(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            print(email)
            if usertype == 'admin':
                e1 = request.POST['T1']
                print(e1)
                return render(request, 'AddBalance.html', {'e1': e1})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AddBalance1(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == "admin":
                obj1 = tdata()
                e1 = request.POST['T1']
                amount = request.POST['T2']
                date = request.POST['T3']
                remark = request.POST['T4']
                obj = userdata.objects.get(email=e1)
                obj1.id = obj1.id
                obj1.email = e1
                obj1.amount = amount
                obj1.date = date
                obj1.remark = remark
                obj1.transaction = "Credit"
                print(obj.balance)
                print(amount)
                a = int(obj.balance)
                b = int(amount)
                ans = a + b
                obj.balance = ans
                obj.save()
                obj1.save()

                return render(request, 'AddBalance1.html', {'msg': "Amount Add Success"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ShowByAdminTransaction(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                e1 = request.POST['T1']
                print(e1)
                obj = tdata.objects.filter(email=e1)
                data = obj
                return render(request, 'ShowByAdminTransaction.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ShowTransaction(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            obj = tdata.objects.filter(email=email)
            obj1 = userdata.objects.filter(email=email)
            obj3 = cartdata.objects.filter(email=email)

            data = obj
            datas = obj1
            data3 = obj3
            i = 0
            for d in data3:
                l = d.item_name
                i = i + 1
            print(i)
            return render(request, 'ShowTransaction.html', {'data': data, 'datas': datas, 'count': i})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def EditTransaction(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                id = request.POST['T1']
                obj = tdata.objects.filter(id=id)
                data = obj
                return render(request, 'EditTransaction.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def EditTransaction1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                id = request.POST['T1']
                obj = tdata.objects.get(id=id)

                amount = request.POST['T2']
                date = request.POST['T3']
                transaction = request.POST['T4']
                remark = request.POST['T5']

                obj.amount = amount
                obj.date = date
                obj.transaction = transaction
                obj.remark = remark
                obj.save()
                return render(request, 'EditTransaction1.html', {'msg': "Save Success"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def DeleteTransaction(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                id = request.POST['T1']
                obj = tdata.objects.filter(id=id)
                data = obj
                return render(request, 'DeleteTransaction.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def DeleteTransaction1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                id = request.POST['T1']
                obj = tdata.objects.filter(id=id)
                obj.delete()
                return render(request, 'DeleteTransaction1.html', {'msg': "Delete Success"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AddItem(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            return render(request, 'AddItem.html', {'email': email})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AddItem1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            obj = itemdata()
            a = request.POST['T1']
            b = request.POST['T2']
            c = request.POST['T3']
            upload_file = request.FILES['F1']
            print(upload_file)
            path = os.path.basename(upload_file.name)
            file_ext = os.path.splitext(path)[1][1:]
            filename = str(int(time.time())) + '.' + file_ext
            fs = FileSystemStorage()
            fs.save(filename, upload_file)
            obj.photo = filename
            obj.item_name = a
            obj.item_description = b
            obj.item_price = c
            obj.save()
            return render(request, 'AddItem.html', {'msg': "Add Item Success"})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def ShowItem(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            obj2 = itemdata.objects.filter()
            data = obj2
            if data:
                return render(request, 'ShowItem.html', {'data': data})
            else:
                return render(request, 'ShowItem.html', {'msg': "Data Not Found"})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def EditItem(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                a = request.POST['T1']
                obj = itemdata.objects.filter(item_name=a)
                data = obj
                return render(request, 'EditItem.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def EditItem1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            if request.method == 'POST':
                a = request.POST['T1']
                b = request.POST['T2']
                c = request.POST['T3']
                upload_file = request.FILES['F1']
                obj = itemdata.objects.get(item_name=a)
                print(upload_file)
                path = os.path.basename(upload_file.name)
                file_ext = os.path.splitext(path)[1][1:]
                filename = str(int(time.time())) + '.' + file_ext
                fs = FileSystemStorage()
                fs.save(filename, upload_file)
                obj.photo = filename
                obj.item_name = a
                obj.item_description = b
                obj.item_price = c
                obj.save()
                return render(request, 'EditItem1.html', {'msg': "Edit Item Success"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def DeleteItem(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == 'admin':
                a = request.POST['T1']
                obj = itemdata.objects.filter(item_name=a)
                data = obj
                return render(request, 'DeleteItem.html', {'data': data})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def DeleteItem1(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'admin':
            a = request.POST['T1']
            obj = itemdata.objects.get(item_name=a)
            obj.delete()
            return render(request, 'DeleteItem1.html', {'msg': "Delete Item Success"})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def AddToCart(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            if request.method == 'POST':
                obj = cartdata()
                name = request.POST['T2']
                desc = request.POST['T3']
                price = request.POST['T4']
                quantity = 1

                upload_file = request.POST['T5']
                print(upload_file)
                obj.photo = upload_file
                obj.email = email
                obj.item_name = name
                obj.item_description = desc
                obj.item_price = price
                obj.main_price = price
                obj.quantity = quantity
                print(email)
                print(name)
                obj.save()
                return HttpResponseRedirect('../Product/')
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('AuthError')
    else:
        return HttpResponseRedirect


def plus(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            if request.method == 'POST':
                name = request.POST['T1']
                price = request.POST['T2']
                quantity = request.POST['T3']

                obj = cartdata.objects.get(item_name=name, email=email)

                obj.quantity = int(obj.quantity) + 1
                obj.item_price = int(obj.item_price) + int(price)
                obj.save()
                return HttpResponseRedirect('/ShowCart/')
            else:
                return HttpResponseRedirect('AuthError')
        else:
            return HttpResponseRedirect('AuthError')
    else:
        return HttpResponseRedirect('AuthError')


def minus(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            if request.method == 'POST':
                name = request.POST['T1']
                price = request.POST['T2']
                quantity = request.POST['T3']
                obj = cartdata.objects.get(item_name=name, email=email)
                obj.quantity = int(obj.quantity) - 1
                print(obj.quantity)
                if obj.quantity == 0:
                    obj.delete()
                else:
                    obj.item_price = int(obj.item_price) - int(price)
                    obj.save()
                return HttpResponseRedirect('/ShowCart/')
            else:
                return HttpResponseRedirect('AuthError')
        else:
            return HttpResponseRedirect('AuthError')
    else:
        return HttpResponseRedirect('AuthError')


def ShowCart(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        if usertype == 'user':
            obj = cartdata.objects.filter(email=email)
            obj3 = userdata.objects.filter(email=email)
            datas = obj3
            data = obj
            i = 0
            for d in data:
                l = d.item_name
                i = i + 1
            print(i)

            if data:
                total = 0
                for d in data:
                    total = total + d.item_price
                    obj2 = itemdata.objects.filter(item_name=d.item_name)
                    data2 = obj2
                return render(request, 'ShowCart.html',
                              {'data': data, 'total': total, 'data2': data2, 'datas': datas, 'count': i})
            else:
                return render(request, 'ShowCart.html',
                              {'msg': 'You have not cart item please add to card item', 'datas': datas, 'count': i})
        else:
            return HttpResponseRedirect('AuthError')
    else:
        return HttpResponseRedirect('AuthError')


def Pay(request):
    if request.method == "POST":
        if request.session.has_key('usertype'):
            usertype = request.session['usertype']
            email = request.session['email']
            if usertype == "user":
                obj1 = tdata()
                amount = request.POST['T2']

                date = request.POST['T3']
                obj = userdata.objects.get(email=email)
                obj1.id = obj1.id
                obj1.email = email
                obj1.amount = amount
                obj1.date = date
                obj1.remark = "Wallet"
                obj1.transaction = "Debit"
                print(obj.balance)
                print(amount)
                a = int(obj.balance)
                b = int(amount)
                if a >= b:
                    ans = a - b
                    obj.balance = ans

                    obj.save()
                    obj1.save()
                    obj2 = cartdata.objects.filter()
                    obj5 = ordersdata()
                    for d in obj2:
                        obj5.item_name = d.item_name
                        obj5.user_email = email
                        obj5.price = d.main_price
                        obj5.quantity = d.quantity
                        obj5.order_date = date
                        obj5.request = "Pending"
                        obj5.save()
                    obj2.delete()
                    return render(request, 'Pay.html', {'msg': "Payment Success"})
                else:
                    return render(request, 'Pay.html', {'msg': "You have not Balance"})
            else:
                return HttpResponseRedirect('/AuthError/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def Orders(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        print(usertype)
        if usertype == 'user':
            obj = ordersdata.objects.filter(user_email=email)
            datas = userdata.objects.filter(email=email)
            datad = cartdata.objects.filter(email=email)
            if obj:
                i = 0
                for d in datad:
                    l = d.item_name
                    i = i + 1
                print(i)
                return render(request, 'Orders.html', {'data': obj, 'datas': datas, 'count': i, })
            else:
                i = 0
                for d in datad:
                    l = d.item_name
                    i = i + 1
                print(i)
                return render(request, 'Orders.html',
                              {'datas': datas, 'count': i, 'msg': 'You have not Order item please add to card item'})

        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('AuthError')


def Home(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        print(usertype)
        if usertype == 'admin':
            obj = ordersdata.objects.filter()
            data = obj
            msg = "No orders"
            return render(request, 'Home.html', {'data': data, 'msg': msg})
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def Confirm(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        print(usertype)
        if usertype == 'admin':
            order_id = request.POST['T1']
            obj = ordersdata.objects.get(order_id=order_id)
            obj.request = "Success ✔"
            obj.save()
            return HttpResponseRedirect('/Home/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')


def Reject(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        email = request.session['email']
        print(usertype)
        if usertype == 'admin':
            order_id = request.POST['T1']
            price = request.POST['T2']
            quantity = request.POST['T3']
            date = request.POST['T4']
            print(order_id)
            print(price)
            print(quantity)
            print(date)
            obj = ordersdata.objects.get(order_id=order_id)

            obj.request = "Faild ❌"
            obj.save()
            obj = userdata.objects.get(email=obj.user_email)
            p = int(price) * int(quantity)
            obj2 = tdata()
            obj2.amount = p
            obj2.date = date
            obj2.transaction = 'Credit'
            obj2.remark = 'UPI'
            obj.balance = int(obj.balance) + int(p)
            obj.save()
            obj2.save()

            return HttpResponseRedirect('/Home/')
        else:
            return HttpResponseRedirect('/AuthError/')
    else:
        return HttpResponseRedirect('/AuthError/')
