# Copyright (c) 2024, yugandhara and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airline(Document):
	# In your custom app's migration file


	def execute():
		if not frappe.db.exists("Custom Field", "Airline-website"):
			frappe.get_doc({
				"doctype": "Custom Field",
				"dt": "Airline",
				"fieldname": "website",
				"label": "Website",
				"fieldtype": "Data",
				"insert_after": "name"  # or wherever you want to place it
			}).insert()

