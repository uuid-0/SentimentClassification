from fastapi import FastAPI, WebSocket
from celery_worker import celery_app
from celery.result import AsyncResult
from celery_worker import analyze_sentiment

app = FastAPI()


@app.post("/analyze-sentiment/")
async def analyze(text: str):
    task = analyze_sentiment.delay(text)
    return {"task_id": task.id}


@app.get("/task/{task_id}")
async def get_task(task_id: str):
    task = AsyncResult(task_id, app=celery_app)
    if task.ready():
        return {"status": "completed", "result": task.result}
    else:
        return {"status": "pending"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
