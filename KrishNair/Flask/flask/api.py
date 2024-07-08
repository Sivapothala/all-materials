## Put and Delete - HTTP Verbs
## working with API's -- Json

from flask import Flask, jsonify,request

app = Flask(__name__)

##Initial Data in my to do list
items = [
{"id": 1, "name": "Item 1", "description": "This is item 1"},
{"id": 2, "name": "Item 2", "description": "This is item 2"}

]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List"

## Get : all the Items

@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

##Retrive item by specified id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_itembyid(item_id):
    item = next((item for item in items if item["id"] == item_id ),None)
    if item is None:
        return jsonify("Error : item not found")
    return jsonify(item)

##Retrive item by specified id
@app.route("/items",methods=['POST'])
def createitem():
    if not request.json or not 'name' in request.json:
        return jsonify("Error : item not found")
    new_item ={
        "id" : items[-1]["id"]+1 if items else 1,
        "name" : request.json["name"],
        "description" : request.json.get("description","")
    }
    items.append(new_item)
    return jsonify(new_item)


## Put : Update an existing item
@app.route("/items/<int:item_id>",methods=['PUT'])
def Edititem(item_id):
    item = next((item for item in items if item["id"] == item_id ),None)
    if item is None:
        return jsonify("Error : item not found")
    item["name"] = request.json.get("name",item["name"])
    item["description"] = request.json.get("description",item["description"])
    return jsonify(item)

### Delete : Delete an item
@app.route("/items/<int:item_id>",methods=['DELETE'])
def Deleteitem(item_id):
    item = next((item for item in items if item["id"] == item_id ),None)
    if item is None:
        return jsonify("Error : item not found")
    items.remove(item)
    return jsonify({"result":"Item Deleted"})

if __name__ == "__main__":
    app.run(debug=True)