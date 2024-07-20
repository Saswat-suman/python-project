#from flask import Flask
#from models import db,Employee
#from routes import main
#from config import Config

from __init__ import create_app
from models import db
app = create_app()
db.init_(app)

with app.app_context():
    db.create_all()



if __name__ == "__main__":
    app.run(debug=True)