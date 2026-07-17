from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import json

# Initialize Gemini Client (Placeholder for GitHub)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

app = FastAPI()

# Allow frontend cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserProfile(BaseModel):
    raw_data: str

@app.post("/api/generate-cv")
async def generate_cv(profile: UserProfile):
    prompt = f"""
    You are an expert ATS and Career Coach. Parse this raw data into a digital CV.
    Raw Data: {profile.raw_data}
    
    Output STRICT JSON with the keys: 
    "professional_headline", "executive_summary", "core_competencies" (array of strings), "suggested_icebreaker".
    """
    
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", 
            generation_config={"response_mime_type": "application/json"}
        )
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}
