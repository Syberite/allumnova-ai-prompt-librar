# Database Schema Integration Mapping

To ensure seamless integration between the Gemini API JSON outputs and the Allumnova backend, the following schema mapping has been established for our relational database (MySQL/MariaDB).

## 1. Digital CV Output -> `user_profiles` Table
When the AI generates the Bio & Headline JSON, the data will be parsed and updated into the core user table.
*   `AI JSON: "professional_headline"` ➔ `DB: user_profiles.headline (VARCHAR 255)`
*   `AI JSON: "executive_summary"` ➔ `DB: user_profiles.bio (TEXT)`
*   `AI JSON: "core_competencies"` ➔ `DB: user_skills` (Mapped via a one-to-many relationship using `user_id` and `skill_name`).

## 2. ATS Resume Review Output -> `resume_evaluations` Table
For caching match scores so we don't have to ping the LLM repeatedly for the same job posting.
*   `AI JSON: "match_score"` ➔ `DB: resume_evaluations.score (INT)`
*   `AI JSON: "missing_keywords"` ➔ `DB: resume_evaluations.missing_tags (JSON)`

By structuring the backend to accept these exact keys, we eliminate the need for complex middleware parsing. The Python API bridge can execute standard `UPDATE` or `INSERT` SQL queries directly using the LLM's strict JSON response.
