def validate_symbol(symbol):
    return symbol.upper().endswith("USDT")

def validate_quantity(quantity):
    try:
        return float(quantity) > 0
    except:
        return False

def validate_price(price):
    try:
        return float(price) > 0
    except:
        return False
