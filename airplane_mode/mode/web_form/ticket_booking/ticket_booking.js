frappe.ready(function() {

    frappe.web_form.on('flight', (field, value) => {

        if (value) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Airplane Flight',
                    name: value
                },
                callback: function(r) {
                    if (r.message) {

                        let departure_time = r.message.time_of_departure|| null;
                        if (departure_time) {
                            const timeParts = departure_time.split(":");
                            if (timeParts.length === 3) {
                                departure_time = `${timeParts[0].padStart(2, '0')}:${timeParts[1].padStart(2, '0')}:${timeParts[2].padStart(2, '0')}`;
                            } else {
                                console.error("Invalid time format:", departure_time);
                                departure_time = ''; 
                            }
                        }
                        frappe.web_form.set_value('source_airport_code', r.message.source_airport_code || '');
                        frappe.web_form.set_value('destination_airport_code', r.message.destination_airport_code || '');
                        frappe.web_form.set_value('departure_date', r.message.date_of_departure);
                        frappe.web_form.set_value('departure_time', departure_time);
                        frappe.web_form.set_value('duration_of_flight', r.message.duration );
                        frappe.web_form.set_value('gate_number', r.message.gate_number );
                        frappe.web_form.set_value('flight_price', r.message.flight_price);
                    } else {
                        console.error("No data found for the selected flight.");
                    }
                }
            });
        }
    });
});
