"""
Advanced conversational AI agent with context management
Real customer service behavior with proper dialogue handling
"""
from sentence_transformers import SentenceTransformer
import numpy as np
import random
from datetime import datetime
from config import Config
from knowledge_base import AGENTS, COMPANY_INFO, CONVERSATION_PATTERNS

class CustomerCareAgent:
    """
    Professional customer care agent with:
    - Multi-turn conversation management
    - Context awareness
    - Intent recognition
    - Personalized responses
    - Follow-up suggestions
    """
    
    def __init__(self):
        print("\n Initializing Thoughtful AI Customer Care Agent...")
        
        # Load semantic search model
        print(f" Loading model: {Config.EMBEDDING_MODEL}")
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)
        
        # Build searchable knowledge base
        self._build_knowledge_base()
        
        # Conversation state management
        self.conversation_context = {
            "mentioned_agents": [],
            "topics_discussed": [],
            "user_intent": None,
            "last_agent_discussed": None
        }
        
        # Initialize LLM for complex queries
        self.llm = self._setup_llm()
        
        # Analytics
        self.metrics = {
            "queries": 0,
            "agent_inquiries": 0,
            "company_inquiries": 0,
            "llm_fallbacks": 0
        }
        
        print(" Customer Care Agent ready!\n")
    
    def _build_knowledge_base(self):
        """Build comprehensive searchable knowledge base"""
        self.kb_entries = []
        self.kb_responses = []
        self.kb_types = []
        
        # Add all agent information
        for agent_id, agent_data in AGENTS.items():
            # Main description
            self.kb_entries.append(f"What does {agent_data['name']} do?")
            self.kb_responses.append({
                "type": "agent",
                "agent_id": agent_id,
                "content": agent_data['description'],
                "data": agent_data
            })
            self.kb_types.append("agent_description")
            
            # Benefits
            benefits_text = f"Benefits of {agent_data['name']}: " + ", ".join(agent_data['benefits'])
            self.kb_entries.append(benefits_text)
            self.kb_responses.append({
                "type": "agent_benefits",
                "agent_id": agent_id,
                "content": benefits_text,
                "data": agent_data
            })
            self.kb_types.append("agent_benefits")
        
        # Add company information
        self.kb_entries.append("Tell me about Thoughtful AI")
        self.kb_responses.append({
            "type": "company",
            "content": COMPANY_INFO["overview"]["description"],
            "data": COMPANY_INFO["overview"]
        })
        self.kb_types.append("company")
        
        # Add benefits information
        self.kb_entries.append("What are the benefits of using Thoughtful AI?")
        self.kb_responses.append({
            "type": "benefits",
            "content": self._format_benefits(),
            "data": COMPANY_INFO["benefits"]
        })
        self.kb_types.append("benefits")
        
        # Pre-compute embeddings
        print(f" Indexing {len(self.kb_entries)} knowledge entries...")
        self.kb_embeddings = self.model.encode(
            self.kb_entries,
            show_progress_bar=False,
            normalize_embeddings=True
        )
        print(f"   ✓ Knowledge base ready with {len(self.kb_entries)} entries")
    
    def _format_benefits(self):
        """Format company benefits nicely"""
        benefits = COMPANY_INFO["benefits"]
        return f"""Using Thoughtful AI's platform delivers transformational results:

• **Cost Savings**: {benefits['cost_savings']}
• **Denial Reduction**: {benefits['denial_reduction']}
• **Efficiency**: {benefits['efficiency']}
• **Accuracy**: {benefits['accuracy']}
• **Speed**: {benefits['speed']}
• **Scalability**: {benefits['scalability']}

Our AI agents handle the entire revenue cycle, freeing your team to focus on patient care."""
    
    def _setup_llm(self):
        """Setup LLM with fallback"""
        try:
            if Config.GROQ_API_KEY:
                from groq import Groq
                print(" LLM: Connected to Groq")
                return Groq(api_key=Config.GROQ_API_KEY)
            elif Config.OPENAI_API_KEY:
                from openai import OpenAI
                print(" LLM: Connected to OpenAI")
                return OpenAI(api_key=Config.OPENAI_API_KEY)
        except Exception as e:
            print(f"  LLM unavailable: {e}")
        return None
    
    def _detect_intent(self, query):
        """Detect user intent from query"""
        query_lower = query.lower()
        
        # Check conversation patterns
        for intent, pattern_data in CONVERSATION_PATTERNS.items():
            patterns = pattern_data.get("patterns", [])
            for pattern in patterns:
                if pattern in query_lower:
                    return intent
        
        # Check for specific agent mentions
        for agent_id, agent_data in AGENTS.items():
            agent_name = agent_id.lower()
            if agent_name in query_lower:
                return f"agent_{agent_id}"
        
        # Check for general topics
        if any(word in query_lower for word in ["all", "agents", "products", "suite", "platform"]):
            return "product_overview"
        
        return "general"
    
    def _handle_conversation_pattern(self, intent):
        """Handle predefined conversation patterns"""
        pattern_data = CONVERSATION_PATTERNS.get(intent)
        if not pattern_data:
            return None
        
        response = pattern_data.get("response")
        if response:
            return response
        
        # Handle multiple response options (like greetings)
        responses = pattern_data.get("responses", [])
        if responses:
            return random.choice(responses)
        
        return None
    
    def _search_knowledge_base(self, query):
        """Semantic search with context awareness"""
        try:
            # Encode query
            query_emb = self.model.encode(
                query,
                show_progress_bar=False,
                normalize_embeddings=True
            )
            
            # Compute similarities
            similarities = np.dot(self.kb_embeddings, query_emb)
            
            # Boost based on conversation context
            if self.conversation_context["last_agent_discussed"]:
                last_agent = self.conversation_context["last_agent_discussed"]
                for idx, response in enumerate(self.kb_responses):
                    if response.get("agent_id") == last_agent:
                        similarities[idx] *= 1.2  # Boost related content
            
            # Get best match
            best_idx = similarities.argmax()
            confidence = float(similarities[best_idx])
            
            if confidence >= Config.SIMILARITY_THRESHOLD:
                return self.kb_responses[best_idx], confidence
            
            return None, confidence
            
        except Exception as e:
            print(f" Search error: {e}")
            return None, 0.0
    
    def _format_agent_response(self, agent_data, query_lower):
        """Format detailed agent response based on what user asked"""
        agent = agent_data["data"]
        response = f"**{agent['full_name']}**\n\n{agent['description']}\n\n"
        
        # Add benefits if asked
        if any(word in query_lower for word in ["benefit", "advantage", "why", "help"]):
            response += "**Key Benefits:**\n"
            for benefit in agent['benefits'][:4]:  # Top 4
                response += f"• {benefit}\n"
            response += "\n"
        
        # Add use cases if relevant
        if any(word in query_lower for word in ["use", "case", "scenario", "when", "example"]):
            response += "**Common Use Cases:**\n"
            for use_case in agent['use_cases']:
                response += f"• {use_case}\n"
            response += "\n"
        
        # Update context
        self.conversation_context["last_agent_discussed"] = agent_data["agent_id"]
        if agent_data["agent_id"] not in self.conversation_context["mentioned_agents"]:
            self.conversation_context["mentioned_agents"].append(agent_data["agent_id"])
        
        return response.strip()
    
    def _get_follow_up_suggestions(self):
        """Suggest relevant follow-up questions"""
        suggestions = []
        
        # If discussed specific agent, suggest related agents
        if self.conversation_context["last_agent_discussed"]:
            other_agents = [aid for aid in AGENTS.keys() 
                          if aid not in self.conversation_context["mentioned_agents"]]
            if other_agents:
                agent = AGENTS[other_agents[0]]
                suggestions.append(f"Learn about {agent['name']}")
        
        # General suggestions
        if len(self.conversation_context["mentioned_agents"]) == 0:
            suggestions.append("What are all your AI agents?")
        
        if "pricing" not in self.conversation_context["topics_discussed"]:
            suggestions.append("How much does it cost?")
        
        if "demo" not in self.conversation_context["topics_discussed"]:
            suggestions.append("Can I see a demo?")
        
        return suggestions[:2]  # Max 2 suggestions
    
    def _llm_fallback(self, query, history):
        """Use LLM for questions outside knowledge base"""
        if not self.llm:
            return "I specialize in Thoughtful AI's healthcare automation platform. Ask me about our AI agents (EVA, CAM, PHIL, DANA, etc.), pricing, demos, or how we can help your organization!"
        
        try:
            # Build context-aware prompt
            system_prompt = f"""You are a helpful customer service agent for Thoughtful AI, a healthcare RCM automation company.

Our products: EVA (eligibility verification), CAM (claims processing), PHIL (payment posting), DANA (denial management), Prior Authorization Agent, Medical Coding Agent.

Key facts:
- 95%+ accuracy, 75% denial reduction, 95% cost savings
- AI Operating System for healthcare RCM
- Integrates with major EHR/EMR systems
- Trusted by leading healthcare providers

Be friendly, concise, and helpful. If asked about our products, provide accurate info. For general questions, answer helpfully but briefly."""
            
            messages = [{"role": "system", "content": system_prompt}]
            
            # Add recent history
            for msg in history[-5:]:
                if msg.get("role") in ["user", "assistant"]:
                    messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
            
            messages.append({"role": "user", "content": query})
            
            response = self.llm.chat.completions.create(
                model=Config.LLM_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            
            self.metrics["llm_fallbacks"] += 1
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I'm having trouble right now, but I'm here to help with Thoughtful AI questions! Ask me about our agents or request a demo. (Error: {str(e)})"
    
    def chat(self, message, history):
        """Main chat interface with full conversation management"""
        self.metrics["queries"] += 1
        
        if not message or not message.strip():
            return "I'm here to help! Ask me about Thoughtful AI's agents, pricing, demos, or how we can transform your RCM operations."
        
        message = message.strip()
        query_lower = message.lower()
        
        # Detect intent
        intent = self._detect_intent(message)
        self.conversation_context["user_intent"] = intent
        
        # Handle conversation patterns (greetings, pricing, etc.)
        pattern_response = self._handle_conversation_pattern(intent)
        if pattern_response:
            if intent not in self.conversation_context["topics_discussed"]:
                self.conversation_context["topics_discussed"].append(intent)
            return pattern_response
        
        # Search knowledge base
        result, confidence = self._search_knowledge_base(message)
        
        if result:
            # Found good match
            if result["type"] == "agent" or result["type"] == "agent_benefits":
                self.metrics["agent_inquiries"] += 1
                response = self._format_agent_response(result, query_lower)
            else:
                self.metrics["company_inquiries"] += 1
                response = result["content"]
            
            # Add confidence indicator
            if Config.CONFIDENCE_DISPLAY:
                response += f"\n\n*[Confidence: {confidence:.1%}]*"
            
            # Add follow-up suggestions
            suggestions = self._get_follow_up_suggestions()
            if suggestions:
                response += "\n\n**You might also want to know:**\n"
                for suggestion in suggestions:
                    response += f"• {suggestion}\n"
            
            return response
        
        # Fallback to LLM
        return self._llm_fallback(message, history)
    
    def get_all_agents_overview(self):
        """Return overview of all agents"""
        overview = "**Thoughtful AI's Complete Agent Suite:**\n\n"
        for agent_id, agent in AGENTS.items():
            overview += f"**{agent['full_name']}**\n{agent['description']}\n\n"
        return overview
