from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logger.error("OPENAI_API_KEY is not set in the environment variables")
    raise ValueError("OPENAI_API_KEY is not set")

client = AsyncOpenAI(api_key=OPENAI_API_KEY)
logger.info(f"OPENAI_API_KEY is set: {OPENAI_API_KEY[:5]}...")

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        logger.info(f"Received chat request: {data}")

        async def event_stream():
            try:
                stream = await client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=data['messages'],
                    stream=True
                )
                async for chunk in stream:
                    if await request.is_disconnected():
                        logger.info("Client disconnected, stopping stream")
                        break
                    content = chunk.choices[0].delta.content
                    if content is not None:
                        yield f"data: {json.dumps({'content': content})}\n\n"
            except Exception as e:
                logger.error(f"Error in event stream: {str(e)}")
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)