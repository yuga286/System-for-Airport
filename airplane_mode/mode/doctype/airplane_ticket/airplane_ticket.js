// Copyright (c) 2024, yugandhara and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });




frappe.ui.form.on('Airplane Ticket', {
    validate: function(frm) {
        // Ensure the flight field is present and has a value
        if (!frm.doc.flight) {
            frappe.throw("Flight field is missing or not selected.");
        }
        
        // Fetch the airplane flight document based on the flight reference
        frappe.db.get_doc("Airplane Flight", frm.doc.flight).then((airplane_flight_doc) => {
            // Check if the airplane flight has an associated airplane
            if (!airplane_flight_doc.airplane) {
                frappe.throw("The selected flight does not have an associated airplane.");
            }

            // Fetch the airplane document to get the seat capacity
            return frappe.db.get_doc("Airplane", airplane_flight_doc.airplane);
        }).then((airplane) => {
            const capacity = airplane.capacity;

            // Count the number of tickets already issued for this flight
            return frappe.db.count("Airplane Ticket", { filters: { flight: frm.doc.flight } });
        }).then((current_ticket_count) => {
            // Compare current tickets with the airplane's capacity
            if (current_ticket_count >= capacity) {
                frappe.throw(`No more tickets can be issued. The airplane's capacity of ${capacity} seats is full.`);
            }
        });
    },

    refresh: function(frm) {
        // Add custom button
        frm.add_custom_button(__('Set Seat'), () => {
            // Save the form first
            frm.save();

            // Create a new dialog
            let d = new frappe.ui.Dialog({
                title: 'Set Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Submit',
                primary_action(values) {
                    // Set the seat field with the input value
                    frm.set_value('seat', values.seat_number);
                    // Close the dialog
                    d.hide();
                }
            });

            // Show the dialog
            d.show();
        }, "Actions");
    }
});
