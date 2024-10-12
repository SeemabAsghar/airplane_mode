# Copyright (c) 2024, seemi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
    pass
    def on_submit(self):
        self.status=="Completed"