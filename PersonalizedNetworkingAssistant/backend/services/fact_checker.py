import wikipedia


def fact_check_topic(topic: str):
    try:
        summary = wikipedia.summary(topic, sentences=2)

        return {
            "topic": topic,
            "summary": summary
        }

    except Exception:
        return {
            "topic": topic,
            "summary": "No information found."
        }