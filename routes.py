from flask import redirect, render_template, request, session, flash
from app import app
import users
import center_info
import string

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/proposition")
def new():
    return render_template("center_proposition.html")


@app.route("/skicenters")
def skicenters():
    list = center_info.get_list()
    return render_template("skicenters.html", list = list)

@app.route("/info/<int:skicenter_id>")
def info(skicenter_id):
    info = center_info.get_info(skicenter_id)
    print(info)
    return render_template("info.html", skicenter_id=info[0][0], name=info[0][1], slopes=info[0][2], lifts=info[0][3], info=info)

@app.route("/login",methods=["GET","POST"])
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
    return redirect("/login")

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
            return render_template("error.html", message = "Salasanat eroavat toisistaan!")
        if len(password1) < 8:
       	    return render_template("error.html", message = "Salasana on liian lyhyt. Sen tulee olla vähintään 8 merkkiä!")
        if password1 == "":
           return render_template("error.html", message = "Salasana ei voi olla tyhjä..")
        if not set(list(string.digits)).intersection(password1):
            return render_template("error.html", message = "Salasanan tulee sisältää vähintään yksi numero!")


        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message = "Tuntematon käyttjärooli")

        if users.register(username, password1, role):
            return redirect("/skicenters")
        else: 
            return render_template("error.html", message = "Rekisteröinti ei onnistunut. Käyttäjänimi mahdollisesti jo käytössä. Kokeilethan jotain toista.")
#

