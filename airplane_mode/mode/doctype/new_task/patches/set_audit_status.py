import frappe

def do_execute():
    # set all task "audit_status" based on "audit_completed" 
    task=frappe.get_all("New Task",fields=["name","audit_completed"])
    for t in task:
        if t.audit_completed==1:
            frappe.log_error("Task is completed",t.name)
            frappe.db.set_value("New Task", t.name, "audit_status", "Completed",update_modified=1)
            frappe.db.commit()
        else:
            frappe.db.set_value("New Task", t.name, "audit_status", "Not Started",update_modified=1)
            frappe.db.commit()