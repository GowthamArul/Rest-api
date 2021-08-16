from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# From Server End, not from browser end
# POST - used to receive data
# Get - used to send data back only

# Post /store data: {name:}
@app.route('/store', methods=['POST']) # By default it will use "GET" request, so we have specified both "POST and GET" request in the methods
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# Get /store/<string:name>
@app.route('/store/<string:name>') # 'https://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # this will conver the store dictionary values into a JSON

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST']) # 'https://127.0.0.1:5000/store/some_name'
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # 'https://127.0.0.1:5000/store/some_name'
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message' : 'store not found'})
    

app.run(port=5000)