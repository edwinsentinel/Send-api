import unittest
import json
from api.version1.all_orders import app

class TestOrders(unittest.TestCase):
	"""This class tests order creation"""
	def setUp(self):
		self.api = app
		self.client = self.api.test_client()

		self.new_order1 = {
			"parcelID" : 1,
			"sender_name" : "Barbz",
			"sender_email" : "barbz2@gmail.com.com",
			"pick_up" : "Eldy",
			"drop_off" : "Kitale",
			"recipient_name" : "Edwin Waweru",
			"weight" : 56,
			"cost" : 2000,
			"status" : "Delivered"
		}
	"""Test order creation"""
	def test_create_order(self):
		result = self.client.post('/api/v1/create_order', data = json.dumps(self.new_order1), content_type='application/json')
		self.assertEqual(result.status_code, 201)