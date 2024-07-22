from destiny.WMAP.server import *

class User(db.model):
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

class Vulners(db.model):
    id = db.Column(db.integer, primary_key=True)
    cve_id = db.Column(db.String, unique=True, nullable=False)


with app.app_context():
    db.create_all()