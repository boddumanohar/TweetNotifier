from app import db,User, Handle
db.create_all()
avi = User(user_id=123456)
db.session.add(avi)
db.session.commit()