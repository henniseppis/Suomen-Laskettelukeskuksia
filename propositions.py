from db import db
from sqlalchemy.sql import text
import users 
from sqlalchemy.sql import text

def save_new(center):
    user = users.user_id()
    if user == 0:
    	return False
    sql = text("INSERT INTO propositions (name, user_id) VALUES (:center, :user)")
    db.session.execute(sql, {"center":center, "user":user})
    db.session.commit()
    return True
    
def read():
    sql = text("SELECT id, name FROM propositions ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def delete(center_id):
    print(center_id)
    sql = text("DELETE FROM propositions WHERE id=:center_id")
    print("onnistui")
    db.session.execute(sql, {"center_id":center_id})
    db.session.commit()
