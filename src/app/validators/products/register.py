from cerberus import Validator

def register_validator (product: dict):
    register_validator = Validator({
        "name": {"type": "string", "required": True, "minlength": 2, "maxlength": 100},
        "supplier": {"type": "string", "required": True, "minlength": 2, "maxlength": 100},
        "supplier_cnpj": {"type": "string", "required": True, "length": 14},
        "sku": {"type": "string", "required": True, "minlength": 3, "maxlength": 50},
        "qnty": {"type": "integer", "required": True, "min": 0},
        "position": {"type": "string", "required": True, "minlength": 1, "maxlength": 100},
        "stoke_level": {"type": "integer", "required": True, "min": 0},
        "supply_data": {"type": "dict", "required": True},
        "daily_departure": {"type": "dict", "required": True},
        "monthly_departure": {"type": "integer", "required": True, "min": 0}
    })
    
    product = register_validator.validate(product)
    
    if product is False:
        raise ValueError("Invalid data")
