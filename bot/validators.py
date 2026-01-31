def validate(symbol, side, type, quantity, price):
    if type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")