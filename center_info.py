from db import db
from sqlalchemy.sql import text



def get_list():
    sql = text("SELECT name, location FROM skicenters ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_info():
    sql = text("SELECT s.name, i.slopes, i.lifts FROM skicenters s, info i ORDER BY s.id")
    result = db.session.execute(sql)
    return result.fetchall()
