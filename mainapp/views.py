# Create your views here.
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from datetime import datetime 
from .models import *
from django.contrib import messages

import pandas
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"You don't have account with this username or password !")
            return redirect('login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email is already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)               
                user.save()   
                return redirect('login')
        else:
            messages.info(request,' Password is not same Please enter correct password')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def predict(request):
    return render(request, 'predict.html')


def result(request):
    data = pandas.read_csv("C:\\Users\\vipin\\OneDrive\\Desktop\\diabeties.csv")

    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    X_train

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    result1 = ""
    if prediction == [1]:
        result1 = "YOU MAY HAVE DIABETIES "
    else:
        result1 = "YOU ARE HEALTHY"
    return render(request, 'predict.html', {"result2": result1})



def heart(request):
    return render(request, 'heart.html')


def res1(request):
    data =pandas.read_csv("C:\\Users\\vipin\\OneDrive\\Desktop\\heart.csv")

    X = data.drop("target", axis=1)
    Y = data["target"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    X_train

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n9'])
    val2 = float(request.GET['n10'])
    val3 = float(request.GET['n11'])
    val4 = float(request.GET['n12'])
    val5 = float(request.GET['n13'])
    val6 = float(request.GET['n14'])
    val7 = float(request.GET['n15'])
    val8 = float(request.GET['n16'])
    val9 = float(request.GET['n17'])
    val10 = float(request.GET['n18'])
    val11 = float(request.GET['n19'])   
    val12 = float(request.GET['n20'])
    val13 = float(request.GET['n21'])

    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,val9,val10,val11,val12,val13]])
    result1 = ""

    if prediction == [1]:
        result1 = " YOU MAY HAVE Heart diesease"
        
    else:
        
        result1 = "YOU ARE HEALTHY"
    return render(request, 'heart.html', {"result2": result1})

def cancer(request):
    return render(request, 'cancer.html')

def res2(request):
    data = pandas.read_csv("D:\final\machine learning\breast-cancer.csv")

    X = data.drop("outcome", axis=1)
    Y = data["outcome"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    X_train


    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(request.GET['n9'])
    val2 = float(request.GET['n10'])
    val3 = float(request.GET['n11'])
    val4 = float(request.GET['n12'])
    val5 = float(request.GET['n13'])
    val6 = float(request.GET['n14'])
    val7 = float(request.GET['n15'])
    val8 = float(request.GET['n16'])
    val9 = float(request.GET['n17'])
    val10 = float(request.GET['n18'])
   
    
    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8,val9,val10]])
    result1 = ""
    if prediction == [0]:
        result1 = " YOU MAY HAVE CANCER "
    else:
        result1 = "YOU ARE HEALTHY"
    return render(request, 'predict.html', {"result2": result1}) 


def logout(request):
    auth.logout(request)
    return redirect('/')
