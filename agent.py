from config import Config
from knowledge_base import AGENTS, COMPANY_INFO, CONVERSATION_PATTERNS

class CustomerCareAgent:
    def __init__(self):
        print("Initializing agent...")
        self.system_prompt = self._build_knowledge()
        self.llm = self._init_llm()
        print("Agent ready\n")

    def _build_knowledge(self):
        knowledge = "You are a Thoughtful AI customer service expert.\n\n"
        knowledge += "COMPANY: " + COMPANY_INFO["overview"]["description"] + "\n\n"
        knowledge += "AGENTS:\n"
        for agent_id, agent in AGENTS.items():
            knowledge += "{}: {}\n".format(agent['full_name'], agent['description'])
            knowledge += "Benefits: " + ", ".join(agent['benefits'][:3]) + "\n\n"
        knowledge += "PRICING: Customized based on organization size and needs.\n"
        knowledge += "DEMOS: Available - personalized to your specialty.\n"
        knowledge += "ROI: 300-500% in first year, 95% cost reduction.\n\n"
        knowledge += "Answer questions naturally and helpfully."
        return knowledge

    def _init_llm(self):
        try:
            from groq import Groq
            if Config.GROQ_API_KEY and len(Config.GROQ_API_KEY) > 10:
                print("Groq connected")
                return Groq(api_key=Config.GROQ_API_KEY)
            print("ERROR: No valid API key")
            return None
        except Exception as e:
            print("ERROR:", e)
            return None

    def chat(self, message, history):
        if not message.strip():
            return "How can I help you?"

        if not self.llm:
            return "API key not configured. Add your Groq key to config.py"

        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            for msg in history[-10:]:
                if msg.get("role") in ["user", "assistant"]:
                    messages.append({"role": msg["role"], "content": msg["content"]})
            messages.append({"role": "user", "content": message})

            response = self.llm.chat.completions.create(
                model=Config.LLM_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=400
            )
            return response.choices[0].message.content
        except Exception as e:
            return "Error: {}".format(str(e))

    def get_all_agents_overview(self):
        overview = "Thoughtful AI Agents:\n\n"
        for agent_id, agent in AGENTS.items():
            overview += "{}\n{}\n\n".format(agent['full_name'], agent['description'])
        return overview

    def get_stats(self):
        return {"status": "running"}
