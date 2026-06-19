# Week 2: Prompt Validation Data

To validate the System Prompts and ensure strict JSON outputs without hallucination, the following dummy data was used during manual testing.

## 1. Raw User Profile Data (JSON)
*Used to test the Digital CV Generator and Resume Review Assistant.*

```json
{
  "user_id": "usr_88392",
  "full_name": "Arjun Sharma",
  "education": [
    {
      "institution": "Harcourt Butler Technical University (HBTU)",
      "degree": "B.Tech in Information Technology",
      "expected_graduation": "2027"
    }
  ],
  "technical_skills": [
    "C++",
    "JavaScript",
    "Python",
    "Data Structures & Algorithms",
    "Git",
    "Neovim"
  ],
  "projects": [
    {
      "title": "Smart Campus Job Allocator",
      "description": "Built a full-stack web application to allocate on-campus tasks to students. Implemented the backend logic using Node.js and managed state on the frontend."
    },
    {
      "title": "Algorithm Practice Tracker",
      "description": "Developed a CLI tool to track daily problem-solving streaks across competitive programming platforms like LeetCode and CSES."
    }
  ],
  "experience": [],
  "achievements": [
    "Solved 300+ algorithmic problems online",
    "Top 10% in college hackathon 2025"
  ]
}</digital_cv>
<job_description> 
**Role:** Software Engineering Intern (Summer 2026)
**Company:** TechNova Solutions

**About the Role:**
We are looking for a passionate Software Engineering Intern to join our core product team. You will assist in developing scalable backend services and optimizing our frontend user experience.

**Requirements:**
- Currently pursuing a degree in Computer Science, Information Technology, or a related field.
- Strong foundation in Data Structures and Algorithms.
- Proficiency in C++ or Python.
- Experience with modern web technologies (React, Node.js) is a huge plus.
- Excellent problem-solving skills and a strong desire to learn.
- Familiarity with version control (Git) and collaborative development.
</job_description>

Compare the user's profile against the job description. Identify missing keywords, suggest specific bullet point improvements, and provide a match percentage.

STRICT OUTPUT FORMAT:
You must return your response strictly as a JSON object. Do not include any markdown formatting, conversational text, or explanations outside the JSON.

{
  "match_score": "Percentage (e.g., 75%)",
  "missing_keywords": ["Keyword 1", "Keyword 2"],
  "actionable_improvements": [
    "Suggestion to improve bullet point X",
    "Suggestion to highlight skill Y"
  ]
}
