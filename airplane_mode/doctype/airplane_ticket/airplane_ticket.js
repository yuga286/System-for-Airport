// Copyright (c) 2024, yugandhara and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });




frappe.ui.form.on('Airplane Ticket', {
    validate: function(frm) {
        if (!frm.doc.flight) {
            frappe.throw("Flight field is missing or not selected.");
        }
        
        frappe.db.get_doc("Airplane Flight", frm.doc.flight).then((airplane_flight_doc) => {
            if (!airplane_flight_doc.airplane) {
                frappe.throw("The selected flight does not have an associated airplane.");
            }
            return frappe.db.get_doc("Airplane", airplane_flight_doc.airplane);
        }).then((airplane) => {
            const capacity = airplane.capacity;
            return frappe.db.count("Airplane Ticket", { filters: { flight: frm.doc.flight } });
        }).then((current_ticket_count) => {
            if (current_ticket_count >= capacity) {
                frappe.throw(`No more tickets can be issued. The airplane's capacity of ${capacity} seats is full.`);
            }
        });
    },

    refresh: function(frm) {
        frm.add_custom_button(__('Set Seat'), () => {
            frm.save();
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
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            d.show();
        }, "Actions");
    }
});
