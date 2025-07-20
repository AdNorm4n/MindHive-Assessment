from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from app.planner import detect_intent, extract_slots
from app.tools.calculator import safe_calculate
from app.tools.zus_tools import get_outlet_hours, get_product_info

load_dotenv()

app = FastAPI()

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(user_input: UserMessage):
    user_message = user_input.message
    intent = detect_intent(user_message)
    slots = extract_slots(user_message, intent)

    if intent == "calculator":
        if "expression" not in slots:
            return {"response": "Can you tell me the numbers or expression you want to calculate?"}
        expression = slots["expression"]
        result = safe_calculate(expression)
        return {"response": f"The result of `{expression}` is `{result}`"}

    elif intent == "outlet_info":
        if "location" not in slots or slots["location"] is None:
            return {"response": "Which outlet are you referring to?"}
        location = slots["location"]
        hours = get_outlet_hours(location)
        return {"response": f"{location} outlet hours: {hours}"}

    elif intent == "product_info":
        if "product" not in slots or slots["product"] is None:
            return {"response": "Which product would you like to know about?"}
        product_name = slots["product"]
        info = get_product_info(product_name)
        return {"response": info}

    else:
        return {"response": "I'm sorry, I didn’t understand that. Can you rephrase?"}
