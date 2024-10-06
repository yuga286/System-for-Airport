// Copyright (c) 2024, yugandhara and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             // Add a website link to the sidebar
//             frm.sidebar.add_user_action(__('Official Website'), function() {
//                 window.open(frm.doc.website, '_blank');
//             });
//         }
//     }
// });

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            // Add a website link to the sidebar
            frm.sidebar.add_user_action(__('Official Website'), function() {
                window.open(frm.doc.website, '_blank');
            });
            
            // Add a website link to the form as well
            frm.add_web_link(__('Official Website'), frm.doc.website);
        }
    }
});

// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             // Add a web link with a '#' placeholder
//             frm.sidebar.add_web_link(__('Official Website'), '#').on('click', function() {
//                 if (frm.doc.website) {
//                     window.open(frm.doc.website, '_blank'); // Open the website in a new tab
//                 }
//             });
//         }
//     }
// });

// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             frm.add_custom_button(__('Open Official Website','#'), function() {
//                 window.open(frm.doc.website, '_blank');
//             });
//         }
//     }
// });

// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             // Add the link to the sidebar
//             frm.sidebar.add_web_link(__('Open Official Website','#'), function() {
//                 window.open(frm.doc.website, '_blank');
//             });
//         }
//     }
// });


// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             // Add a web link to the form
//             frm.add_web_link(web(frm)); // Just use frm.doc.website directly

//             // Call the function to add the sidebar action
//             // web(frm);
//         }
//     }
// });


