from flask_restful import Resource, reqparse
from flask_jwt import jwt_required,current_identity

from models.itemModel import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help="This field cannot be Blank"
    )
    parser.add_argument('store_id',
        type=int,
        required = True,
        help="Every item needs a store id"
    )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'msg':'Not found'}, 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'msg': f'An Item with name {name} already exist'}
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
            return item.json()
        except :
            return {'msg': "An error occured"}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
        return {'message': 'Item Deleted'}, 204

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()

class Items(Resource):
    def get(self):
        return {"items" : [item.json() for item in ItemModel.query.all()]}