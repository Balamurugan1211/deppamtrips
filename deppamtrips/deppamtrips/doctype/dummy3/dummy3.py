# Copyright (c) 2023, bramachandran@techfinite.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Dummy3(Document):
    def validate(self):
        frappe.get_doc({"doctype":"ToDo","description":"Hello"}).insert()
