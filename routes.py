from flask import redirect, render_template, request, session, flash
from app import app
import users
import center_info
import string
import tkinter
from tkinter import messagebox

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skicenters")
def skicenters():
    list = center_info.get_list()
    return render_template("skicenters.html", list = list)

@app.route("/info")
def info():
    info = center_info.get_info()
    return render_template("info.html", info=info)

@app.route("/login_plain")
def login_plain():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    if users.login(username, password):
    	return redirect("/skicenters")
    else: 
        return render_template("error.html", message ="Käyttäjätunnusta ei ole" )
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/login_plain")

@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 5 or len(username) > 20:
            return render_template("error.html", message="Käyttäjätunnuksen tulee olla vähintään 5 ja enintään 20 merkkiä. Palaathan takaisin ja kokeilet jotain muuta käyttäjänimeä :)")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            flash('Out of stock! We have only 5 products in stock.', 'error')
        if len(password1) < 8:
       	    messagebox.showinfo("Virhe", "Salasanan tulee olla vähintään 8 merkkiä")
        if password1 == "":
            return render_template("error.html", message="Salasana ei voi olla tyhjä..")
        if not set(list(string.digits)).intersection(password1):
            return render_template("error.html", message="Salasanan tulee sisältää vähintään yksi numero") 

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if users.register(username, password1, role):
            return redirect("/skicenters")
        #else: 
        #    return render_template("error.html", message = "Rekisteröinti ei onnistunut")
#

