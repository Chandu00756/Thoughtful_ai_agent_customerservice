# Thoughtful AI Support Agent

Simple customer support chatbot with semantic search + LLM fallback.

## How it works

1. User asks a question
2. Bot searches knowledge base using semantic similarity
3. If match found (>40% confidence) → return predefined answer
4. If no match → use LLM (Groq) for general questions

## Setup on Replit

### Step 1: Upload files
- Copy `main.py` to your Repl
- Copy `requirements.txt` to your Repl

### Step 2: Add API key (optional)
In Replit Secrets tab, add:
- Key: `GROQ_API_KEY`
- Value: your key from https://console.groq.com/keys

### Step 3: Run
Click the Run button

That's it!

## Testing

Try these:
- "What does EVA do?" → Should match knowledge base
- "Tell me about PHIL" → Should match knowledge base
- "What's 2+2?" → Should use LLM fallback
- "" → Should ask for input

## Tech stack

- **Gradio**: UI framework
- **sentence-transformers**: Semantic search
- **Groq**: Fast LLM inference (free tier)

## How I built it

Used semantic similarity to match user questions against predefined Q&A pairs. 
If similarity score is high enough, return the predefined answer. 
Otherwise, fallback to LLM for general questions.

This approach ensures accurate answers for company-specific questions while 
still being helpful for general queries.
