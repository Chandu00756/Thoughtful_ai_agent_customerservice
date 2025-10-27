"""
Comprehensive Thoughtful AI knowledge base
All products, agents, features, and common customer queries
"""

# Complete agent catalog
AGENTS = {
    "EVA": {
        "name": "Eligibility Verification Agent (EVA)",
        "full_name": "EVA - Eligibility Verification Agent",
        "description": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
        "benefits": [
            "Real-time eligibility verification",
            "Eliminates manual data entry errors",
            "Reduces claim rejections by up to 75%",
            "Integrates with major payer portals",
            "Handles complex multi-payer scenarios"
        ],
        "use_cases": [
            "Patient check-in verification",
            "Pre-service eligibility checks",
            "Benefits verification",
            "Coverage confirmation"
        ],
        "keywords": ["eligibility", "verification", "insurance", "benefits", "coverage", "patient"]
    },
    
    "CAM": {
        "name": "Claims Processing Agent (CAM)",
        "full_name": "CAM - Claims Processing Agent",
        "description": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
        "benefits": [
            "Automated claims submission",
            "95%+ accuracy rate",
            "Reduces manual intervention by 90%",
            "Accelerates reimbursement cycles",
            "Intelligent error detection and correction",
            "Handles complex claim scenarios"
        ],
        "use_cases": [
            "Claims submission",
            "Claims status tracking",
            "Resubmission management",
            "Error correction automation"
        ],
        "keywords": ["claims", "processing", "submission", "reimbursement", "billing"]
    },
    
    "PHIL": {
        "name": "Payment Posting Agent (PHIL)",
        "full_name": "PHIL - Payment Posting Agent",
        "description": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
        "benefits": [
            "Automated payment posting",
            "Fast and accurate reconciliation",
            "Reduces administrative burden by 80%",
            "Handles EOBs and ERAs automatically",
            "Real-time payment tracking"
        ],
        "use_cases": [
            "Payment posting",
            "EOB processing",
            "Payment reconciliation",
            "Account balance updates"
        ],
        "keywords": ["payment", "posting", "reconciliation", "phil", "accounts", "eob", "era"]
    },
    
    "DANA": {
        "name": "Denial Management Agent (DANA)",
        "full_name": "DANA - Denial Management Agent",
        "description": "DANA intelligently manages claim denials, automatically identifies root causes, generates appeals, and resubmits claims to maximize revenue recovery.",
        "benefits": [
            "Automatic denial identification",
            "Root cause analysis",
            "Intelligent appeal generation",
            "Automated resubmission",
            "Reduces denials by 75%",
            "Tracks denial trends"
        ],
        "use_cases": [
            "Denial analysis",
            "Appeal letter generation",
            "Claim resubmission",
            "Denial trend reporting"
        ],
        "keywords": ["denial", "appeals", "rejection", "dana", "resubmission"]
    },
    
    "PREAUTH": {
        "name": "Prior Authorization Agent",
        "full_name": "Prior Authorization Agent",
        "description": "Automates the prior authorization process, reducing wait times from days to minutes and ensuring patients get timely care.",
        "benefits": [
            "Reduces authorization time by 95%",
            "Automated submission to payers",
            "Real-time status tracking",
            "Handles complex medical necessity documentation",
            "Reduces authorization delays"
        ],
        "use_cases": [
            "Prior authorization requests",
            "Medical necessity documentation",
            "Authorization status tracking",
            "Payer communication"
        ],
        "keywords": ["prior authorization", "preauth", "authorization", "approval", "medical necessity"]
    },
    
    "CODING": {
        "name": "Medical Coding Agent",
        "full_name": "Medical Coding Agent",
        "description": "AI-powered medical coding that ensures accuracy, compliance, and optimal reimbursement with automated CPT, ICD-10, and modifier assignment.",
        "benefits": [
            "99%+ coding accuracy",
            "Automatic CPT and ICD-10 assignment",
            "Compliance with latest guidelines",
            "Optimizes reimbursement",
            "Reduces coding backlogs"
        ],
        "use_cases": [
            "Medical record coding",
            "Procedure code assignment",
            "Diagnosis coding",
            "Modifier selection"
        ],
        "keywords": ["coding", "medical coding", "cpt", "icd-10", "icd", "modifiers", "diagnosis"]
    }
}

# Company information
COMPANY_INFO = {
    "overview": {
        "description": "Thoughtful AI delivers the world's first AI operating system for healthcare Revenue Cycle Management (RCM) teams. Our fully human-capable AI Agents transform revenue cycle management end-to-end.",
        "mission": "We're on a mission to fix the U.S. Healthcare System by cutting out the RCM bureaucracy and enabling providers to focus on what matters most: patient care.",
        "achievements": [
            "95%+ accuracy across all AI agents",
            "75% reduction in preventable claim denials",
            "95% reduction in operating expenses",
            "Trusted by leading healthcare providers nationwide",
            "Recent $20 million funding round"
        ]
    },
    
    "benefits": {
        "cost_savings": "Reduce RCM operating expenses by up to 95%",
        "denial_reduction": "Cut preventable claim denials by 75%",
        "efficiency": "Free up staff to focus on patient care instead of administrative tasks",
        "accuracy": "Achieve 95%+ accuracy across all revenue cycle processes",
        "speed": "Accelerate reimbursement cycles and cash flow",
        "scalability": "Scale RCM capabilities without adding headcount"
    },
    
    "technology": {
        "platform": "AI Operating System for Healthcare RCM",
        "capabilities": [
            "Fully autonomous AI agents",
            "Real-time reporting and analytics",
            "Predictive intelligence for denial prevention",
            "Seamless integration with existing systems",
            "Continuous learning and improvement"
        ],
        "differentiators": [
            "End-to-end RCM automation",
            "Human-capable AI agents (not just task automation)",
            "Real-time insights and predictive analytics",
            "Works with existing systems - no rip and replace"
        ]
    },
    
    "customers": {
        "types": [
            "Hospital systems",
            "Medical practices",
            "Behavioral health organizations",
            "Specialty clinics",
            "Dental practices",
            "Therapy centers"
        ],
        "examples": [
            "People's Care",
            "Behavioral Health Works",
            "Proliance Surgeons",
            "Ally Pediatric Therapy",
            "MB2 Dental",
            "Trumpet Behavioral Health"
        ]
    }
}

# Common questions and contextual responses
CONVERSATION_PATTERNS = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "responses": [
            "Hello! I'm your Thoughtful AI support specialist. How can I help you today?",
            "Hi there! Welcome to Thoughtful AI. What can I assist you with?",
            "Good day! I'm here to help you learn about Thoughtful AI's healthcare automation solutions. What would you like to know?"
        ]
    },
    
    "pricing": {
        "patterns": ["price", "cost", "pricing", "how much", "expensive", "afford", "budget"],
        "response": "Our pricing is customized based on your organization's size, needs, and current RCM volume. We offer flexible models including per-transaction pricing and subscription plans. I'd be happy to connect you with our sales team for a personalized quote. Would you like me to arrange that?"
    },
    
    "demo": {
        "patterns": ["demo", "see it", "show me", "trial", "test", "try"],
        "response": "Great! We offer personalized demos tailored to your organization's specific needs. Our demos typically show real-world scenarios from your specialty and demonstrate ROI projections. Would you like to schedule a demo with our team?"
    },
    
    "integration": {
        "patterns": ["integrate", "integration", "connect", "ehr", "emr", "system", "software"],
        "response": "Our AI agents integrate seamlessly with major EHR/EMR systems, practice management platforms, and billing software. We support Epic, Cerner, Athenahealth, eClinicalWorks, and many others. The integration typically takes 2-4 weeks and doesn't require replacing your existing systems. What system are you currently using?"
    },
    
    "implementation": {
        "patterns": ["implement", "setup", "onboard", "start", "begin", "deploy"],
        "response": "Implementation typically takes 4-8 weeks depending on your organization's complexity. Our process includes: system integration, agent configuration, staff training, pilot testing, and full deployment. We provide dedicated support throughout. What's your timeline for getting started?"
    },
    
    "comparison": {
        "patterns": ["vs", "versus", "compare", "difference", "better than", "alternative"],
        "response": "Unlike traditional RPA or task automation, our AI agents are fully autonomous and can handle complex decision-making, exceptions, and edge cases - just like human staff. They learn and improve over time, handle unstructured data, and adapt to changes without reprogramming. What specific comparison would you like to understand?"
    },
    
    "roi": {
        "patterns": ["roi", "return", "savings", "value", "worth it"],
        "response": "Organizations typically see 300-500% ROI within the first year through: 95% reduction in operating costs, 75% fewer denials, 50% faster reimbursements, and elimination of costly errors. Most clients achieve full payback in 3-6 months. Would you like a customized ROI analysis for your organization?"
    }
}
