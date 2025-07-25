from django.contrib import admin
from django.contrib.auth.models import User
from django.template.context_processors import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app1.views import *


urlpatterns=[
    path('admin/',admin.site.urls),
    path('',index),
    path('about/',about),
    path('price/',price),
    path('bread/',bread),
    path('featured/',featured),
    path('contact/',contact),
    path('login/',login),
    path('logout/',logout),
    path('AdminHome/',AdminHome),
    path('UserHome/',UserHome),
    path('AuthError/',AuthError),
    path('AdminReg/',AdminReg),
    path('ShowAdmins/',ShowAdmins),
    path('UserReg/', UserReg),
    path('ShowUser/',ShowUser),
    path('EditUser/',EditUser),
    path('EditUser1/',EditUser1),
    path('DeleteUser/',DeleteUser),
    path('DeleteUser1/',DeleteUser1),
    path('Home/',Home),
    path('AdminPhotoUpload/',AdminPhotoUpload),
    path('AdminPhotoUpload1/',AdminPhotoUpload1),
    path('UserPhotoUpload/', UserPhotoUpload),
    path('UserPhotoUpload1/', UserPhotoUpload1),
    path('EditAdminProfile/',EditAdminProfile),
    path('EditAdminProfile1/',EditAdminProfile1),
    path('EditUserProfile/',EditUserProfile),
    path('EditUserProfile1/',EditUserProfile1),
    path('ChangeAdminPassword/',ChangeAdminPassword),
    path('ChangeAdminPassword1/',ChangeAdminPassword1),
    path('ChangeUserPassword/', ChangeUserPassword),
    path('ChangeUserPassword1/', ChangeUserPassword1),
    path('AddBalance/',AddBalance),
    path('AddBalance1/',AddBalance1),
    path('ShowByAdminTransaction/',ShowByAdminTransaction),
    path('ShowTransaction/',ShowTransaction),
    path('EditTransaction/',EditTransaction),
    path('EditTransaction1/',EditTransaction1),
    path('DeleteTransaction/',DeleteTransaction),
    path('DeleteTransaction1/',DeleteTransaction1),
    path('AddItem/',AddItem),
    path('AddItem1/',AddItem1),
    path('ShowItem/',ShowItem),
    path('EditItem/',EditItem),
    path('EditItem1/',EditItem1),
    path('DeleteItem/',DeleteItem),
    path('DeleteItem1/',DeleteItem1),
    path('AddToCart/',AddToCart),
    path('ShowCart/',ShowCart),
    path('plus/',plus),
    path('minus/',minus),
    path('Pay/',Pay),
    path('Product/',Product),
    path('Orders/',Orders),
    path('Confirm/',Confirm),
    path('Reject/',Reject),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
