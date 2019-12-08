from flask_restful import Resource
from models.storeModel import StoreModel

class StoreResource(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store :
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f"A store with {name} already exist"}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except :
            return {'message':"A error occured"}
        return store.json(),  201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}