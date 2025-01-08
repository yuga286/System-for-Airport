# Copyright (c) 2024, yugandhara and contributors
# For license information, please see license.txt


import frappe


def execute(filters=None):
	columns= [{
		"fieldname": "airplane",
		"label": "Airline",
		"fieldtype": "data"
	},
	{
		"fieldname": "revenue",
		"label": "Revenue",
		"fieldtype": "Currency",
		"options": "INR"
	}]
	
	
	data = frappe.get_all("Airplane Ticket",
	fields=["sum(flight_price) as 'revenue'", "flight.airplane"],
	filters={"docstatus":1}, group_by="airplane")

	chart = {
		"data" : {
			"labels": [x.airplane[:-4] for x in data],
			"datasets": [{"values": [x.revenue for x in data]}],
		},
		"type": "donut",
	}

	return columns, data, None, chart