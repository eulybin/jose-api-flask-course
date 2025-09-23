from flask import Flask, jsonify, request
from stores import stores


app = Flask(__name__)


@app.get("/store")
def get_stores():
    return jsonify(stores)


# @app.post("/store")
# def add_store():
#     data = request.get_json()
#     new_store = {"store_name": data["store_name"], "items": data["items"]}
#     stores.append(new_store)
#     return jsonify(data), 201


@app.post("/store/<string:store_name>")
def add_store(store_name):
    data = request.get_json()
    for store in stores:
        if store["store_name"] == store_name:
            new_item = {"item_name": data["item_name"], "price": data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "No such store found."}, 404
