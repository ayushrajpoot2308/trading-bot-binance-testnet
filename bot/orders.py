from bot.client import get_client
from bot.validators import validate
from bot.logging_config import logger

def place_order(symbol, side, type, quantity, price=None):
    validate(symbol, side, type, quantity, price)
    client = get_client()
    try:
        logger.info(f"Placing order: {symbol} {side} {type} {quantity} {price}")
        if type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol, side=side, type=type, quantity=quantity
            )
        else:
            order = client.futures_create_order(
                symbol=symbol, side=side, type=type,
                quantity=quantity, price=price, timeInForce="GTC"
            )
        logger.info(f"Order response: {order}")
        print("Order successful:", order)
    except Exception as e:
        logger.error(str(e))
        print("Order failed:", e)