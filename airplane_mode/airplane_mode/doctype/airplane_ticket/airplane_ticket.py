# Copyright (c) 2024, seemi and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
    pass
    def before_save(self):
        self.calculate()
        self.validate()
        self.check_status()
        if not self.seat:  
            self.seat = self.assign_seat()
        
    def calculate(self):
        self.total_addons = sum(addon.amount for addon in self.add_ons)
        self.total_amount = self.flight_price + self.total_addons
        
    def validate(self):
        if self.add_ons:
            unique_addon_types = set()
            duplicates = []

            for addon in self.add_ons:
                if addon.item in unique_addon_types:
                    duplicates.append(addon.item)
                else:
                    unique_addon_types.add(addon.item)

            if duplicates:
                frappe.throw(_("Duplicate add-ons found: {}").format(", ".join(duplicates)))
                 
    def check_status(self):
        if self.status!='Boarded':
            frappe.throw(_("Cannot submit Ticket until status is 'Boarded'."))



    def assign_seat(self):
        row = random.randint(1, 100)  
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E']) 
        return f"{row}{seat_letter}"
    
        