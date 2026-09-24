\# CareerPrep AI



CareerPrep AI is an AI-powered career preparation platform that analyzes a candidate's resume and provides personalized career guidance.



\## Features



\- Resume PDF text extraction

\- AI-powered resume analysis

\- Candidate summary

\- Technical skills identification

\- Strength analysis

\- Skill gap identification

\- Suitable job role suggestions

\- Personalized learning roadmap

\- Interview preparation topics



\## AI Technology



\- Python

\- Ollama

\- Llama 3.2

\- PyPDF



\## Current AI Module



The AI module reads a resume PDF and sends the extracted resume information to a locally running Llama 3.2 model through Ollama.



The AI generates:

\- Candidate Summary

\- Technical Skills

\- Strengths

\- Missing Skills

\- Suitable Job Roles

\- Learning Roadmap

\- Interview Preparation Topics



\## Project Structure



```text

CareerPrep-AI/

│

├── .gitignore

├── README.md

├── test\_ai.py

└── resumes/

&#x20;   └── resume.pdf

