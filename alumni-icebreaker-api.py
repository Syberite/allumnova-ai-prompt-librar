import json
import google.generativeai as genai


genai.configure(api_key="")

def generate_icebreaker():
    print("🚀 Starting Allumnova Alumni Icebreaker API...")

    
    student_data = {
        "name": "Arjun Sharma",
        "major": "Information Technology",
        "interests": ["Backend Development", "MySQL", "Python"]
    }
    
    alumni_data = {
        "name": "Priya Patel",
        "company": "TechNova Solutions",
        "role": "Senior Backend Engineer",
        "university": "HBTU"
    }
    
    prompt = f"""
    You are an expert networking coach. Write a highly personalized cold outreach message from this student to this alumni. 
    Student: {json.dumps(student_data)}
    Alumni: {json.dumps(alumni_data)}
    
    Rules:
    - Highlight their shared university connection.
    - Keep it under 75 words.
    - Output STRICT JSON with keys: "subject_line", "icebreaker_hook", "message_body".
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
    generate_icebreaker()
