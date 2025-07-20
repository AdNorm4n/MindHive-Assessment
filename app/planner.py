import re

def detect_intent(message: str) -> str:
    message = message.lower()
    if any(word in message for word in ["calculate", "+", "-", "*", "/", "what is", "how much"]):
        return "calculator"
    elif any(word in message for word in ["open", "close", "hour", "time", "outlet"]):
        return "outlet_info"
    elif any(word in message for word in ["product", "drink", "menu", "matcha", "latte", "espresso"]):
        return "product_info"
    else:
        return "unknown"

def extract_expression(message: str) -> str:
    pattern = r'[-+*/().\d\s]+'
    match = re.search(pattern, message)
    return match.group().strip() if match else ""

def extract_slots(message: str, intent: str) -> dict:
    slots = {}
    message = message.lower()

    if intent == "calculator":
        slots["expression"] = extract_expression(message)

    elif intent == "outlet_info":
        for loc in ["KL", "Petaling Jaya", "Subang", "Penang"]:
            if loc.lower() in message:
                slots["location"] = loc

    elif intent == "product_info":
        for product in ["matcha", "latte", "americano", "espresso"]:
            if product in message:
                slots["product"] = product

    return slots
