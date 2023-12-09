import os
import torch
from celery import Celery
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# Celery configuration
celery_app = Celery(
    "worker", broker="redis://redis/0", backend="redis://redis/0"
)

# Load pre-trained model and tokenizer
model_name = os.environ.get(
    "MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english"
)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


@celery_app.task
def analyze_sentiment(text: str) -> str:
    logger.info(f"Received task with text: {text}")
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    sentiment = logits.argmax().item()
    label = "positive" if sentiment == 1 else "negative"
    return {"label": label}
