# Copyright (c) 2024, seemi and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class FlightPassenger(Document):
	def before_save(self):
		self.full_name = self.first_name +" "+ self.last_name
