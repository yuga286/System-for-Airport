// Copyright (c) 2024, yugandhara and contributors
// For license information, please see license.txt


frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.sidebar.add_user_action(__('Official Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
            frm.add_web_link(__('Official Website'), frm.doc.website);
        }
    }
});

