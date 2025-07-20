import re

def safe_calculate(expression: str) -> str:
    try:
        # Sanitize: only allow numbers and operators
        if not re.match(r"^[\d+\-*/. ()]+$", expression):
            return "Invalid characters in expression."

        # Evaluate
        result = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except Exception:
        return "Sorry, I couldn't calculate that."
