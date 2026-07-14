import json
import os

FEEDBACK_FILE = "data/feedback.json"


def save_feedback(conversation, feedback):
    data = []

    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            data = json.load(file)

    data.append({
        "conversation": conversation,
        "feedback": feedback
    })

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file, indent=4)