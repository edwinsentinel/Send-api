from api.version1.all_orders import app
from flask import jsonify
from api.version1.all_orders.models import SendItOrders

ordersObject = SendItOrders()
length = ordersObject.get_length()

@app.route('/api/v1/home', methods=['GET'])
def home():
    welcome_message1 = "Hello! Welcome to SendIT - see orders here. "
    return welcome_message1

@app.route('/api/v1/all_orders', methods=['GET'])
def get_all_orders():
    orders = ordersObject.all_orders()
    return jsonify({"orders: " :orders})

@app.route('/api/v1/all_orders/<int:parcelID>', methods=['GET'])
def get_all_orders_by_parcelID(parcelID):
    orders = ordersObject.all_orders_by_parcelID(parcelID)
    return jsonify({"orders: " :orders})

@app.route('/api/v1/all_orders/<string:sender_email>', methods=['GET'])
def get_all_orders_by_sender_email(sender_email):
    orders = ordersObject.all_orders_by_sender_email(sender_email)
    return jsonify({"orders: " :orders})

@app.route('/api/v1/cancel/<int:parcelID>', methods=['PUT'])
def cancel_orders_by_parcelID(parcelID):
    orders = ordersObject.cancel_orders(parcelID)
    return jsonify({"orders: " :orders})

@app.route('/api/v1/create_order', methods=['POST'])
def create_new_order():
    orders = ordersObject.new_orders()
    return jsonify({"orders: " :orders}), 201

