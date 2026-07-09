# 🚀 Allumnova AI Prompt Library & API Pipeline

Welcome to the AI integration repository for **Allumnova**, a platform designed to enhance student career growth and alumni networking. 

This repository contains the foundational **Prompt Engineering Architecture** and **Backend API Pipelines** required to power Allumnova's generative AI features. The system is designed with strict anti-hallucination guardrails, ensuring that the LLM consistently outputs reliable, structured JSON data that can be safely ingested by the frontend UI.

## 🌟 Core AI Features

1. **Digital CV Generator (`core-features/digital-cv-generator.md`)**
   - Transforms raw, fragmented user profile data into a polished, professional summary.
2. **Automated Resume Review Assistant (`resume-review-api.py`)**
   - An ATS-style evaluator that compares a user's digital CV against a target job description, outputting match percentages and missing keywords.
3. **AI Bio & Headline Optimizer (`core-features/bio-optimizer.md`)**
   - Generates catchy, professional profile headlines based on a user's academic and technical background.
4. **Alumni Icebreaker Generator (`core-features/alumni-icebreakers.md`)**
   - Drafts highly personalized cold-outreach messages to alumni based on shared identities and target tech stacks.

## 📁 Repository Structure

```text
├── core-features/             # Markdown files containing strict System Prompts
├── documentation/             # Testing logs, flowcharts, and token optimization docs
├── prototype/                 # Interactive HTML/Tailwind UI frontend prototype
├── api-test.py                # Python script: Digital CV Gemini API integration
├── resume-review-api.py       # Python script: Resume ATS matching logic
└── README.md
