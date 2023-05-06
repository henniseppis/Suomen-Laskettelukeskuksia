from db import db
from sqlalchemy.sql import text
import users


def get_list():
    sql = text("SELECT id, name, location FROM skicenters ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_info(skicenter_id):
    sql = text("SELECT s.id, s.name, i.slopes, i.lifts, i.park, i.description FROM skicenters s, info i WHERE s.id=:skicenter_id and i.skicenter_id=s.id" )
    result = db.session.execute(sql, {"skicenter_id": skicenter_id})
    return result.fetchall()
    
def add_review(center, rate):
    user = users.user_id()
    if user == 0:
    	return False
    sql = text("INSERT INTO reviews (user_id, skicenter_id, stars) VALUES (:user, :center, :rate)")
    db.session.execute(sql, {"user": user, "center": center, "rate": rate} )
    db.session.commit()
    return True

def get_reviews(skicenter_id):
	sql = text("SELECT stars FROM reviews WHERE skicenter_id=:skicenter_id")
	result = db.session.execute(sql, {"skicenter_id":skicenter_id})
	return result.fetchall()
	
def count_average(reviews, skicenter_id):
	total = 0
	for review in reviews:
		total += review[0]
	amount = len(reviews)
	if amount == 0:
		return "Keskusta ei ole vielä arvosteltu"
	else:
		average = total/amount
		return format(average, '.2f')
