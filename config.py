"""
Configuration management with environment variables
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """App configuration from environment variables"""
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Model settings
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    LLM_MODEL = os.getenv("LLM_MODEL", "llama-3.3-70b-versatile")
    
    # Agent behavior
    SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", "0.45"))
    CONFIDENCE_DISPLAY = os.getenv("CONFIDENCE_DISPLAY", "true").lower() == "true"
    MAX_HISTORY = int(os.getenv("MAX_HISTORY", "10"))
    
    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8080"))
    
    @classmethod
    def validate(cls):
        """Validate required configs on startup"""
        if not cls.GROQ_API_KEY and not cls.OPENAI_API_KEY:
            print("  WARNING: No LLM API key found. Will only use knowledge base.")
        
        print(f" Config loaded:")
        print(f"   - Embedding model: {cls.EMBEDDING_MODEL}")
        print(f"   - Similarity threshold: {cls.SIMILARITY_THRESHOLD}")
        print(f"   - LLM available: {'Yes' if cls.GROQ_API_KEY or cls.OPENAI_API_KEY else 'No'}")

# Validate on import
Config.validate()
