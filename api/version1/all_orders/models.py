from api.version1.all_orders import app
from flask import request, jsonify

orders_list = [
		{
			"parcelID" : 1,
			"sender_name" : "Barbz",
			"sender_email" : "barbz2@gmail.com.com",
			"pick_up" : "Eldy",
			"drop_off" : "Kitale",
			"recipient_name" : "Edwin Waweru",
			"weight" : 56,
			"cost" : 2000,
			"status" : "Delivered"
		},
		{
			"parcelID" : 2,
			"sender_name" : "Barbz",
			"sender_email" : "barbz2@gmail.com.com",
			"pick_up" : "Eldy",
			"drop_off" : "Kitale",
			"recipient_name" : "Edwin Waweru",
			"weight" : 56,
			"cost" : 2000,
			"status" : "Delivered"
		}
	]   

class SendItOrders():			
	def get_length(self):
		length = len(orders_list)
		return length

	def all_orders(self):
		if len(orders_list) == 0:
			return {"message" : "No orders in the system"}
		return orders_list

	def all_orders_by_parcelID(self, parcelID):
		order = [order for order in orders_list if order['parcelID'] == parcelID]
		if order:
			return order
		return {"message" : "No orders with that ID"}

	def all_orders_by_sender_email(self, sender_email):
		order = [order for order in orders_list if order['sender_email'] == sender_email]
		if order:
			return order
		return {"message" : "No orders made from that email address"}
		
	def cancel_orders(self, parcelID):
		order = [order for order in orders_list if (order['parcelID'] == parcelID and order['status'] !='Delivered')]
		if order:
			order[0]["status"] = request.json["status"]
			if order[0]["status"] == "Cancelled":
				return order
			
			order[0]["status"] = "Cancelled"
			return order
		return {"message" : "order cannot be cancelled."}

	def new_orders(self):
		
		new_order = {
			"parcelID" : orders_list[-1]['parcelID'] + 1,
			"sender_name" : request.json['sender_name'],
			"sender_email" : request.json['sender_email'],
			"pick_up" : request.json['pick_up'],
			"drop_off" : request.json['drop_off'],
			"recipient_name" : request.json['recipient_name'],
			"weight" : request.json['weight'],
			"cost" : 200,
			"status" : "Order requested"
		} 

		orders_list.append(new_order)

		if  orders_list[-1]["sender_name"] == "" or orders_list[-1]["sender_email"] == "" or orders_list[-1]["pick_up"] == "" or orders_list[-1]["drop_off"] == "" or orders_list[-1]["recipient_name"] == "" or orders_list[-1]["weight"] == "":
			orders_list.pop()
			return {"message" : "fields cannot be empty"}

		if orders_list[-1]["weight"] <= 0:
			orders_list.pop()
			return {"message" : "weight cannot be zero "}
			
		return orders_list[-1]
