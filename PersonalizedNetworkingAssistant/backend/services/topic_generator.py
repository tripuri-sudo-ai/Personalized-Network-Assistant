from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)


def generate_conversation(topic: str):

    prompt = (
        f"Networking conversation starter about {topic}:\n"
        "Person A:"
    )

    result = generator(
        prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=50256
    )

    text = result[0]["generated_text"]

    return text