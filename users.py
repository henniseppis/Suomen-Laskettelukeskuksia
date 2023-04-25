import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

#kissa123

def login(username, password):
    sql = text("SELECT id, password, role FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user[0]
            session["username"] = username
            session["role"] = user[2]
            session["secret_password"] = os.urandom(16).hex()
            return True
        return False


def register(username, password, role):
    hash_value = generate_password_hash(password)
    try:
    	sql = text("""INSERT INTO users (username, password, role)
      	VALUES (:username, :password, :role)""")
    	db.session.execute(sql, {'username':username, 'password':hash_value, 'role':role})
    	db.session.commit()
    except:
    	return False
    return login(username, password)
