from backend.services.event_analyzer import analyze_event as analyze_event_service
from fastapi import APIRouter
from backend.schemas import (
    EventRequest,
    TopicRequest,
    FeedbackRequest
)
from backend.services.topic_generator import generate_conversation as generate_conversation_service
from backend.services.fact_checker import fact_check_topic
from backend.services.history_logger import save_history
from backend.services.feedback_logger import save_feedback
from backend.services.history_logger import get_history
router = APIRouter()


@router.post("/analyze-event")
def analyze(request: EventRequest):
    result = analyze_event_service(request.event_description)
    return result


@router.post("/generate-conversation")
def generate(request: TopicRequest):

    conversation = generate_conversation_service(request.topic)

    save_history(
        event=request.topic,
        interests="",
        conversation=conversation
    )

    return {
        "conversation": conversation
    }


@router.post("/fact-check")
def fact_check(request: TopicRequest):
    return fact_check_topic(request.topic)

@router.get("/history")
def history():
    return get_history()


@router.post("/feedback")
def feedback(request: FeedbackRequest):

    save_feedback(
        request.conversation,
        request.feedback
    )

    return {
        "message": "Feedback Saved Successfully"
    }