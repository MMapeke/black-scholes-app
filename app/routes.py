import os
from app import app
from app.models import model
from flask import render_template, request, redirect
import scipy.stats as st
import math

print(st.norm.cdf(.25))

print(st.norm.cdf(.25))

#need to take inputs for everything. 

@app.route("/index")
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home_page.html')

@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method=="GET":
        print("loading get")
        return render_template('form.html')
    else:
        print("loading request")
        userdata=dict(request.form)
        So=float(userdata['stockCost'])
        Xo=float(userdata['exercisePrice'])
        To=float(userdata['timeUntilExp'])
        ro=float(userdata['riskFreeInterestRate'])
        oo=float(userdata['volatility'])
        return render_template('blackScholes.html',So=So, Xo = Xo, To = To, ro = ro, oo = oo, C=model.blackScholes(
            So, Xo, To, ro, oo))
            
@app.route("/contact")
def contact():
    return render_template("contact.html")
            
@app.route("/list2", methods=["GET", "POST"])
def list_2():
    if request.method=="GET":
        print("loading get")
        return render_template('form2.html')
    else:
        print("loading request")
        userdata=dict(request.form)
        So=float(userdata['stockCost'])
        Xo=float(userdata['exercisePrice'])
        To=float(userdata['timeUntilExp'])
        ro=float(userdata['riskFreeInterestRate'])
        co=float(userdata['optionPrice'])
        return render_template('blackScholes.2.html',So = So, Xo = Xo, To = To, ro = ro, co = co, C=model.revBlackScholes(co,So,Xo,To,ro))




@app.route("/calculator")
def loadScholes():
    return render_template("/form.html")


@app.route('/calculator2')
def formTest():
    return render_template("/form.2.html")
    
@app.route('/history')
def history():
    return render_template("/history.html")

@app.route('/derivations')
def derivations():
    return render_template("derivations.html")
    
@app.route('/contact')
def contactUs():
    return render_template("contact.html")