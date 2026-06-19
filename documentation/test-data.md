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
}
