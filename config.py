import os

class Config:
    GROQ_API_KEY = "api_key_here"

    LLM_MODEL = "llama-3.3-70b-versatile"
    HOST = "0.0.0.0"
    PORT = 8080

Config.GROQ_API_KEY = os.environ.get("GROQ_API_KEY", Config.GROQ_API_KEY)
