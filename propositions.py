from db import db
from sqlalchemy.sql import text
import users 


def save_new(center):
    user = users.user_id()
    if user == 0:
    	return False
    sql = text("INSERT INTO propositions (name, user_id) VALUES (:center, :user)")
    db.session.execute(sql, {"center":center, "user":user})
    db.session.commit()
    return True
    
def read():
    sql = text("SELECT id, name FROM propositions")
    result = db.session.execute(sql)
    return result.fetchall()

def delete(center_id):
	sql = text("DELETE FROM propositions WHERE id=:center_id")
	db.session.execute(sql, {"center_id":center_id})
	db.session.commit()
	
def add_skicenter(name,location):
	try:
		sql_info = text("""INSERT INTO skicenters (name, location) VALUES (:name, :location)""")
		db.session.execute(sql_info, {"name":name, "location":location})
		db.session.commit()	
	except:
		return False
	return True
    	
def add_info(skicenter_id,slopes,lifts,park,description):
	try:
		sql_skicenters = text("INSERT INTO info (skicenter_id, slopes, lifts, park,description) VALUES (:skicenter_id, :slopes, :lifts, :park, :description)")
		db.session.execute(sql_skicenters, {"skicenter_id":skicenter_id, "slopes":slopes, "lifts":lifts, "park":park,"description":description})
		db.session.commit()
		return True
	except:
		return False

def get_skicenter_id(name):
	try:
		sql = text("SELECT id FROM skicenters WHERE name=:name")
		result = db.session.execute(sql, {"name":name})
		return result.fetchone()[0]	
	except:
		return False
    
