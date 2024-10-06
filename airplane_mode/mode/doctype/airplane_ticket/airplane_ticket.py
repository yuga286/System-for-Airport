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
        # Create a set to track unique add-on types
        add_on_items = set()
        unique_add_ons = []

        # Loop through the add-ons in the child table
        for add_on in self.add_ons:
            # If the add-on type is not in the set, add it
            if add_on.item not in add_on_items:
                add_on_items.add(add_on.item)
                unique_add_ons.append(add_on)
            else:
                frappe.msgprint(("Duplicate add-on '{0}' removed.").format(add_on.item))

        # Update the add_ons table with only unique entries
        # self.add_ons = unique_add_ons
        self.set("add_ons", unique_add_ons)

    def calculate_total_amount(self):

        self.remove_duplicate_add_ons()

    # Initialize the total as the Flight Price
        price= self.flight_price or 0  # Handle case where flight_price might be None

        total_amount =price
        # Add the amount of each add-on to the total
        if self.add_ons:
            for add_on in self.add_ons:
                add_on_amount = add_on.amount or 0
                total_amount += add_on_amount

        # Set the Total Amount field
        self.total_amount = total_amount

        return total_amount
    

    
    def before_submit(self):
        # Raise a validation error if the status is not 'Boarded'
        if self.docstatus == 1 and self.status != "Boarded":
            frappe.throw("You cannot submit this ticket because the passenger has not boarded.", frappe.ValidationError)



    
    def before_insert(self):
        # Ensure the flight field is present and has a value
        if not self.flight:
            frappe.throw("Flight field is missing or not selected.")
        
        # Fetch the airplane flight document based on the flight reference
        airplane_flight_doc = frappe.get_doc("Airplane Flight", self.flight)
        
        # Check if the airplane flight has an associated airplane
        if not airplane_flight_doc.airplane:
            frappe.throw("The selected flight does not have an associated airplane.")
        
        # Fetch the airplane document to get the seat capacity
        airplane = frappe.get_doc("Airplane", airplane_flight_doc.airplane)
        capacity = airplane.capacity
        
        # Count the number of tickets already issued for this flight
        current_ticket_count = frappe.db.count("Airplane Ticket", filters={
            "flight": self.flight
        })
        
        # Compare current tickets with the airplane's capacity
        if current_ticket_count >= capacity:
            frappe.throw(f"No more tickets can be issued. The airplane's capacity of {capacity} seats is full.")