// Copyright (c) 2024, yugandhara and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Flight", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Airplane Flight", {
    options: function(frm) {
        if (frm.doc.gate) {
            frappe.db.get_value("Airport", frm.doc.gate, "options", (r) => {
                if (r && r.options) {
                    frm.set_value("gatenumbe", r.options);
                }
            });
        }
    }
});
