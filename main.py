"""
Thoughtful AI Customer Care Agent
Professional conversational interface
"""
import gradio as gr
from agent import CustomerCareAgent, AGENTS
from config import Config

# Initialize agent
print("\n" + "="*60)
agent = CustomerCareAgent()
print("="*60)

# Build interface
with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate"
    ),
    title="Thoughtful AI Customer Care",
    css="""
    .agent-card { padding: 15px; border-radius: 8px; background: #f8f9fa; margin: 10px 0; }
    .metric-box { text-align: center; padding: 10px; }
    """
) as app:
    
    gr.Markdown("""
    #  Thoughtful AI - Customer Care Agent
    
    ### Welcome to Thoughtful AI's Healthcare RCM Automation Platform
    
    I'm your personal AI assistant, trained on our complete product suite. Ask me anything about:
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("""
            **Our AI Agents:**
            -  **EVA** - Eligibility Verification
            -  **CAM** - Claims Processing
            -  **PHIL** - Payment Posting
            -  **DANA** - Denial Management
            -  **Prior Auth** - Authorization
            -  **Medical Coding** - Automated Coding
            """)
        
        with gr.Column(scale=1):
            gr.Markdown("""
            **What I Can Help With:**
            - Product information & features
            - Pricing and ROI analysis
            - Demo scheduling
            - Integration questions
            - Implementation process
            - Customer success stories
            """)
    
    chatbot = gr.Chatbot(
        type="messages",
        height=450,
        show_label=False,
        avatar_images=(
            "https://api.dicebear.com/7.x/avataaars/svg?seed=User",
            "https://api.dicebear.com/7.x/bottts/svg?seed=Thoughtful"
        )
    )
    
    with gr.Row():
        msg_input = gr.Textbox(
            placeholder="Ask me anything about Thoughtful AI...",
            show_label=False,
            scale=4,
            autofocus=True
        )
        send_btn = gr.Button("Send ", scale=1, variant="primary")
    
    with gr.Row():
        clear_btn = gr.Button(" Clear", size="sm")
        all_agents_btn = gr.Button(" Show All Agents", size="sm")
        metrics_btn = gr.Button(" Metrics", size="sm")
    
    info_box = gr.Markdown(visible=False)
    
    gr.Markdown("""
    ---
    
    ###  Try asking:
    """)
    
    gr.Examples(
        examples=[
            "Tell me about all your AI agents",
            "What does EVA do and how can it help my practice?",
            "How much does Thoughtful AI cost?",
            "Can I see a demo?",
            "What's the difference between CAM and PHIL?",
            "How does DANA handle claim denials?",
            "What kind of ROI can I expect?",
            "Do you integrate with Epic?",
            "Tell me about your medical coding agent",
        ],
        inputs=msg_input
    )
    
    # Event handlers
    def respond(message, history):
        bot_response = agent.chat(message, history)
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": bot_response})
        return history, ""
    
    def show_all_agents():
        overview = agent.get_all_agents_overview()
        return gr.update(visible=True, value=overview)
    
    def show_metrics():
        m = agent.metrics
        metrics_text = f"""
 **Session Metrics:**
- Total queries: {m['queries']}
- Agent inquiries: {m['agent_inquiries']}
- Company inquiries: {m['company_inquiries']}
- LLM fallbacks: {m['llm_fallbacks']}

**Context:**
- Agents discussed: {len(agent.conversation_context['mentioned_agents'])}
- Topics covered: {len(agent.conversation_context['topics_discussed'])}
"""
        return gr.update(visible=True, value=metrics_text)
    
    def hide_info():
        return gr.update(visible=False)
    
    # Wire events
    send_btn.click(respond, [msg_input, chatbot], [chatbot, msg_input])
    msg_input.submit(respond, [msg_input, chatbot], [chatbot, msg_input])
    clear_btn.click(lambda: [], None, chatbot).then(hide_info, None, info_box)
    all_agents_btn.click(show_all_agents, None, info_box)
    metrics_btn.click(show_metrics, None, info_box)

if __name__ == "__main__":
    print(f"\n Launching on {Config.HOST}:{Config.PORT}...")
    app.launch(
        server_name=Config.HOST,
        server_port=Config.PORT,
        share=True,
        show_error=True
    )
