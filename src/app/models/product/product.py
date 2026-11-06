from src.app.validators.register_validator import register_validator

class Product:
    def __init__(self,
                 name,
                 supplier,
                 supplier_cnpj,
                 sku,
                 qnty,
                 position,
                 stoke_level,
                 supply_data,
                 daily_departure,
                 monthly_departure
                 ):
        self.name = name
        self.supplier = supplier
        self.supplier_cnpj = supplier_cnpj
        self.sku = sku
        self.qnty = qnty
        self.position = position
        self.stoke_level = stoke_level
        self.supply_data = supply_data
        self.daily_departure = daily_departure
        self.monthly_departure = monthly_departure
        
    def do_dict(self):
        return {
            "name": self.name,
            "supplier": self.supplier,
            "supplier_cnpj": self.supplier_cnpj,
            "sku": self.sku,
            "qnty": self.qnty,
            "position": self.position,
            "stoke_level": self.stoke_level,
            "supply_data": self.supply_data,
            "daily_departure": self.daily_departure,
            "monthly_departure": self.monthly_departure
        }
        

    def validator(self):
        product = self.do_dict()
        return register_validator(product)