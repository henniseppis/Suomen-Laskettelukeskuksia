from db import db
from sqlalchemy.sql import text

def save_review():
    sql = text("""INSERT INTO reviews (deck_id, user_id, stars, comment)
            VALUES (:deck_id, :user_id, :stars, :comment)""")
    