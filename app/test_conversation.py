import requests

BASE_URL = "http://127.0.0.1:8000/chat"

def send(msg):
    return requests.post(BASE_URL, json={"message": msg}).json()["response"]

def test_happy_path():
    print("🟢 Happy Path")
    print("User: Is there an outlet in Petaling Jaya?")
    print("Bot:", send("Is there an outlet in Petaling Jaya?"))

    print("User: SS 2, what’s the opening time?")
    print("Bot:", send("SS 2, what’s the opening time?"))

def test_interrupted_path():
    print("\n🟡 Interrupted Path")
    print("User: Where is the outlet?")
    print("Bot:", send("Where is the outlet?"))

    print("User: Sorry, I meant SS 15 Subang.")
    print("Bot:", send("Sorry, I meant SS 15 Subang."))

if __name__ == "__main__":
    test_happy_path()
    test_interrupted_path()
