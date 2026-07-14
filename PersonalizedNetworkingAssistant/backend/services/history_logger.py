import json
import os

HISTORY_FILE = "data/history.json"


def save_history(event, interests, conversation):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

    history.append({
        "event": event,
        "interests": interests,
        "conversation": conversation
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except:
        return []