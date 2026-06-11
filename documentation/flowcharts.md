# Architecture & Conversational Flow Diagrams

## Feature 1: Digital CV Generation Data Pipeline

[User Inputs Data on Allumnova] 
        │
        ▼
[Backend captures details & formats as JSON] 
        │
        ▼
[JSON injected into 'digital-cv-generator' System Prompt] 
        │
        ▼
[API Request sent to LLM (with strict JSON structural constraints)] 
        │
        ▼
[Backend parses JSON Response] ───(If Parsing Fails)───► [Fallback default profile]
        │
 (If Successful)
        ▼
[Render optimized headlines & bullet points beautifully on User Profile Page]
