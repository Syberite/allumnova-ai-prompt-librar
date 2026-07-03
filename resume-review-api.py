import json
import google.generativeai as genai


genai.configure(api_key="YOUR_GEMINI_API_KEY")

def run_resume_reviewer():
    print("🚀 Starting Allumnova Resume Reviewer API...")

    
    digital_cv = json.dumps({"skills": ["Python", "C++"], "experience": []})
    job_description = "Looking for a backend intern with Node.js and React experience."
    
    
    prompt = f"""
    You are an ATS reviewer. Compare this CV to the Job Description.
    CV: {digital_cv}
    JD: {job_description}
    Output STRICT JSON with keys: "match_score" (percentage), "missing_keywords" (array).
    """

    print("⏳ Pinging Gemini API...")
    
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", 
            generation_config={"response_mime_type": "application/json"}
        )
        response = model.generate_content(prompt)
        print("\n🎉 Output:\n", response.text)
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    run_resume_reviewer()
