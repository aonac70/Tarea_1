from datetime import datetime
from product import Product
from customer import RegularClient


class Sale:
    def __init__(self, client=None):
        self.invoice_number = None
        self.date = datetime.now()
        self.client = client
        self.details = []

    def add_detail(self, product, quantity):
        self.details.append({"product": product, "quantity": quantity})

    def remove_detail(self, product, quantity):
        for detail in self.details:
            if detail["product"] == product:
                detail["quantity"] -= quantity
                if detail["quantity"] <= 0:
                    self.details.remove(detail)
                break
        
    def calculate_total(self):
        subtotal = sum(detail["product"].precio * detail["quantity"] for detail in self.details)
        discount = 0  # You can add discount calculation logic here
        iva = subtotal * 0.12  # Assuming 12% VAT
        total = subtotal - discount + iva
        return subtotal, discount, iva, total

    def load_from_json(self, data):
        self.invoice_number = data["factura"]
        self.date = data["Fecha"]
        # Load client data here if needed
        self.details = [{"product": Product(item["poducto"], item["precio"], 0), "quantity": item["cantidad"]} for item in data["detalle"]]

    def get_json(self):
        json_data = {
            "factura": self.invoice_number,
            "Fecha": self.date,
            "cliente": self.client.fullName() if self.client else None,
            "detalle": [{"id": detail["product"].id, "descripcion": detail["product"].descrip, "precio": detail["product"].preci, "cantidad": detail["quantity"]} for detail in self.details],
        }
        return json_data