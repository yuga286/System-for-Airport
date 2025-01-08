# Copyright (c) 2024, yugandhara and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 150
        },
        {
            "label": "Revenue",
            "fieldname": "total_revenue",
            "fieldtype": "Currency",
            "width": 120
        }
    ]

    data = get_airline_revenue_report()

    total_revenue = sum([row.get('total_revenue', 0) for row in data])
    data.append({
        "airline": "Total",
        "total_revenue": total_revenue
    })

    chart = {
        "data": {
            "labels": [row['airline'] for row in data if row['airline'] != 'Total'],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [row['total_revenue'] for row in data if row['airline'] != 'Total']
                }
            ]
        },
        "type": "donut",
        "title": "Revenue by Airline",
    }

    return columns, data, None, chart

def get_airline_revenue_report():
    query = """
    SELECT 
        a.name AS airline, 
        COALESCE(SUM(at.total_amount), 0) AS total_revenue
    FROM 
        `tabAirline` a
    LEFT JOIN 
        `tabAirplane Ticket` at ON a.name = at.airline
    GROUP BY 
        a.name
    ORDER BY 
        total_revenue DESC
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    return result
