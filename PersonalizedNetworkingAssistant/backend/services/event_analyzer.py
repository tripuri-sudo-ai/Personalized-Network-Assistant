from transformers import pipeline

# DistilBERT Feature Extraction Pipeline
feature_extractor = pipeline(
    task="feature-extraction",
    model="distilbert-base-uncased"
)

KEYWORDS = [
    "Artificial Intelligence",
    "Machine Learning",
    "Healthcare",
    "Education",
    "Cyber Security",
    "Blockchain",
    "Cloud Computing",
    "Finance",
    "Sustainability",
    "Data Science"
]


def analyze_event(event_description: str):

    # Run DistilBERT
    _ = feature_extractor(event_description)

    text = event_description.lower()

    detected = []

    for keyword in KEYWORDS:
        if keyword.lower() in text:
            detected.append(keyword)

    if len(detected) == 0:
        detected.append("General Networking")

    return {
        "themes": detected
    }