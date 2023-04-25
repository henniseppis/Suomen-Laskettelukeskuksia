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
