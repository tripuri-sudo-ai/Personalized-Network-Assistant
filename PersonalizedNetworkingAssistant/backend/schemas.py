from pydantic import BaseModel


class EventRequest(BaseModel):
    event_description: str
    interests: str


class TopicRequest(BaseModel):
    topic: str


class FeedbackRequest(BaseModel):
    conversation: str
    feedback: str