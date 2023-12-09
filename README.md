# FastAPI, Celery, and Redis Project

This project demonstrates a simple but scalable setup using FastAPI, Celery, and Redis, containerized with Docker and orchestrated with Docker Compose. 

## Description

This application is a basic example of how to integrate FastAPI with Celery for background task processing, using Redis as a message broker and result backend. The setup also includes Flower for monitoring the Celery tasks.

## Features

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **Celery**: An asynchronous task queue/job queue based on distributed message passing.
- **Redis**: An in-memory database used as a message broker for Celery.
- **Flower**: A web-based tool for monitoring and administrating Celery clusters.
- **Docker and Docker Compose**: For easy development, deployment, and scaling.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Setting Up

1. **Clone the Repository**

    ```bash
    git clone git@github.com:uuid-0/SentimentClassification.git
    ```

2. **Build and Run with Docker Compose**

    ```bash
    docker-compose up --build
    ```

This command builds the images for your FastAPI application, Celery worker, Redis, and Flower, and then starts the containers.

### Accessing the Application

- FastAPI application will be running at `http://localhost:8000`
- Flower dashboard for monitoring Celery at `http://localhost:5555`

### Structure

- `app/`: FastAPI application code.
- `Dockerfile`: Dockerfile for building the FastAPI application image.
- `docker-compose.yml`: Docker Compose configuration file.
- `requirements.txt`: Python dependencies required for the application.

## Usage

This FastAPI application provides an endpoint for analyzing sentiment in a given text and another endpoint to check the status and result of the analysis.

Analyzing Sentiment

To analyze the sentiment of a text, send a POST request to the /analyze-sentiment/ endpoint with the text as a parameter. This will enqueue the task in Celery for processing.

Endpoint: POST /analyze-sentiment/

Parameter: text - The text for which you want to analyze sentiment.

Example:

```bash
Copy code
curl -X 'POST' \
  'http://localhost:8000/analyze-sentiment/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Your text here"}'
  ```
This will return a JSON response with a task_id, which you can use to check the status of the task.

**Checking Task Status**

To check the status of the sentiment analysis task, send a GET request to the /task/{task_id} endpoint, replacing {task_id} with the ID returned from the /analyze-sentiment/ endpoint.

Endpoint: GET /task/{task_id}
Parameter: task_id - The ID of the task for which you want to check the status.

Example:

```bash
Copy code
curl -X 'GET' \
  'http://localhost:8000/task/<task_id>' \
  -H 'accept: application/json'
  ``````
The response will be a JSON object containing the status of the task. If the task is completed, it will also include the result of the sentiment analysis.

## License

MIT

