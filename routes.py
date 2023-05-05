from flask import redirect, render_template, request, session
from app import app
import users
import center_info
import propositions
import string

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proposition_form")
def proposition_form():
    return render_template("center_proposition.html")
    
@app.route("/proposition", methods=["POST"])
def proposition():
	users.check_csrf()
    center = request.form["center"]
    if len(center) > 50:
        return render_template("error.html", error="Teksti on liian pitkä. Kirjoitathan vain keskuksen nimen ja sijainnin")
    if propositions.save_new(center):
    	return render_template("successful_proposition.html")
    else:
    	return render_template("error.html", message="Toivomus ei tallentunut kokeilethan uudestaan")

@app.route("/read")
def read():
    if users.require_role(2):
    	list = propositions.read()
    	return render_template("read_propositions.html", list=list)
    else:
    	return render_template("error.html", message="Sivun voi nähdä vain ylläpitäjät. Olethan varmasti ylläpitäjä? ")

@app.route("/remove", methods=["POST"])
def remove():
	if users.require_role(2):
		center_id = request.form["proposition"]
		propositions.delete(center_id)
		return redirect("/read")
		
	return render_template("error.html", message="Sivun voi nähdä vain ylläpitäjät. Olethan varmasti ylläpitäjä? ")
	
@app.route("/add_center_form")
def add_center_form():
    return render_template("add_center.html")
    	
@app.route("/add", methods=["POST"])
def add():
	if users.require_role(2):
		name = request.form["center_name"]
		location = request.form["location"]
		lifts = request.form["lifts"]
		slopes = request.form["slopes"]
		description = request.form["description"]
		park = request.form["park"]
		
		if propositions.add_skicenter(name,location):
			skicenter_id = propositions.get_skicenter_id(name)
			propositions.add_info(skicenter_id,slopes,lifts,park,description)
			return render_template("successful_add.html")
		else:
			return render_template("error.html", message="Lisääminen ei onnistunut yritäthän uudestaan. Voi olla että keskus löytyy jo sivuiltamme")
	return render_template("error.html", message="Sivun voi nähdä vain ylläpitäjät. Olethan varmasti ylläpitäjä? ")
	
	
@app.route("/skicenters")
def skicenters():
    list = center_info.get_list()
    return render_template("skicenters.html", list=list)

@app.route("/info/<int:skicenter_id>")
def info(skicenter_id):
	info = center_info.get_info(skicenter_id)
	reviews = center_info.get_reviews(skicenter_id)
	average_rate = center_info.count_average(reviews, skicenter_id)
	return render_template("info.html", skicenter_id=info[0][0], name=info[0][1], slopes=info[0][2], lifts=info[0][3], park=info[0][4], description=info[0][5], rate=average_rate, info=info, reviews=reviews)

@app.route("/review_form")
def review_form():
    list = center_info.get_list()
    return render_template("add_review.html", list=list)

@app.route("/review", methods=["POST"])
def review():
	center = request.form["centers"]
	rate = request.form["rate"]
	if center_info.add_review(center, rate):
		return render_template("successful_review.html")  
	return render_template("error.html", message="Lisääminen ei onnistunut yritäthän uudestaan.")
    
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
    users.logout()
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
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

