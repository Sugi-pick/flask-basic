from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from  resources.item import Item, Items
from resources.store import StoreList, StoreResource

app = Flask(__name__)
app.secret_key = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
api = Api(app)




jwt = JWT(app,authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(StoreResource, '/store/<string:name>')
api.add_resource(Items, "/items")
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

