import frappe

@frappe.whitelist(allow_guest=True)
def get_context(context=None):
	if context is None:
		context={}
	context["airports"] = frappe.get_all('Airport', fields=['name'])
	filters = get_filters()
	context["shops"]= frappe.get_all('Shop Info', filters=filters, fields=['shop_name', 'area_of_the_shop', 'shop_keeper_name', 'shop_number'])
	context["selected_airport"] = frappe.form_dict.get('airport', '')
	return context
	
@frappe.whitelist(allow_guest=True)
def get_filters():
	filters = {'Status': 'Available For lease'} 
	airport = frappe.form_dict.get('airport')

	if airport:
		filters['airport_name'] = airport

	return filters

from frappe.utils import now
from datetime import datetime
def get_deletetask():
	doc=frappe.get_all('Contact Us',fields=['name','creation'])
	today=datetime.now().date()
	for d in doc:
		dg=frappe.get_doc('Contact Us',d['name'])
		if dg.creation:
			creat=dg.creation.date()
			creat_days=(today-creat).days
			if int(creat_days)>=30:
				frappe.delete_doc('Contact Us', d['name'])
				frappe.db.commit()

# http://airport_mode.com/api/v2/mwthod/airplane_mode.airplane_mode.mode.get_context

@frappe.whitelist(allow_guest=True)
def new_doc():
	frappe.masgprint('Hello')