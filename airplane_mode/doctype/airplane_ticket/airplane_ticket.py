# Copyright (c) 2024, yugandhara and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()

    def remove_duplicate_add_ons(self):
        add_on_items = set()
        unique_add_ons = []

        for add_on in self.add_ons:
            if add_on.item not in add_on_items:
                add_on_items.add(add_on.item)
                unique_add_ons.append(add_on)
            else:
                frappe.msgprint(("Duplicate add-on '{0}' removed.").format(add_on.item))

        self.set("add_ons", unique_add_ons)

    def calculate_total_amount(self):
        self.remove_duplicate_add_ons()
        price= self.flight_price or 0  

        total_amount =price
        if self.add_ons:
            for add_on in self.add_ons:
                add_on_amount = add_on.amount or 0
                total_amount += add_on_amount
        self.total_amount = total_amount

        return total_amount
    

    
    def before_submit(self):
        if self.docstatus == 1 and self.status != "Boarded":
            frappe.throw("You cannot submit this ticket because the passenger has not boarded.", frappe.ValidationError)



    
    def before_insert(self):
        if not self.flight:
            frappe.throw("Flight field is missing or not selected.")
        airplane_flight_doc = frappe.get_doc("Airplane Flight", self.flight)
        if not airplane_flight_doc.airplane:
            frappe.throw("The selected flight does not have an associated airplane.")
        
        airplane = frappe.get_doc("Airplane", airplane_flight_doc.airplane)
        capacity = airplane.capacity
        
        current_ticket_count = frappe.db.count("Airplane Ticket", filters={
            "flight": self.flight
        })
        if current_ticket_count >= capacity:
            frappe.throw(f"No more tickets can be issued. The airplane's capacity of {capacity} seats is full.")