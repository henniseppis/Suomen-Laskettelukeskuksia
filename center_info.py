from db import db
from sqlalchemy.sql import text



def get_list():
    sql = text("SELECT id, name, location FROM skicenters ORDER BY id")
    result = db.session.execute(sql)
    return result.fetchall()

def get_info(skicenter_id):
    sql = text("SELECT s.id, s.name, i.slopes, i.lifts FROM skicenters s, info i WHERE s.id=:skicenter_id and i.id=s.id" )
    result = db.session.execute(sql, {"skicenter_id": skicenter_id})
    return result.fetchall()
