import os
import json
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def read_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_digital_cv():
    print("🚀 Starting Allumnova Backend API Test...\n")

  
    prompt_path = "core-features/digital-cv-generator.md"
    try:
        system_prompt = read_prompt(prompt_path)
        print(f"✅ Loaded prompt template from {prompt_path}")
    except FileNotFoundError:
        print(f"❌ Error: Could not find {prompt_path}. Ensure you are in the root directory.")
        return

    
    dummy_user_data = {
        "full_name": "Arjun Sharma",
        "education": "B.Tech in Information Technology",
        "technical_skills": ["C++", "JavaScript", "Python"],
        "projects": ["Smart Campus Job Allocator"]
    }
    
    user_data_str = json.dumps(dummy_user_data, indent=2)


    final_prompt = system_prompt.replace("{{USER_PROFILE_JSON}}", user_data_str)
    print("✅ Injected raw JSON data into the prompt context")


    print("⏳ Pinging LLM API... (Enforcing strict JSON output)")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": final_prompt},
                {"role": "user", "content": "Process the profile data and output the JSON."}
            ],
            response_format={ "type": "json_object" }, 
            temperature=0.2
        )
        
       
        ai_output = response.choices[0].message.content
        print("\n🎉 AI Generation Successful! Backend Output:\n")
        print(ai_output)
        
    except Exception as e:
        print(f"\n❌ API Error: {e}")
        print("Ensure you have replaced 'YOUR_API_KEY_HERE' with a valid key.")

if __name__ == "__main__":
    generate_digital_cv()
