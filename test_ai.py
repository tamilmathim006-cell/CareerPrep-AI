from pypdf import PdfReader
import subprocess

# Read resume
reader = PdfReader("resumes/resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text

print("===== RESUME CONTENT =====")
print(resume_text)

prompt = f"""
You are CareerPrep AI.

Analyze this resume and provide:

1. Candidate Summary
2. Technical Skills
3. Strengths
4. Missing Skills
5. Suitable Job Roles
6. Personalized Learning Roadmap
7. Interview Preparation Topics

Keep the answer simple and useful for a fresher.

Resume:
{resume_text}
"""

print("\n===== CAREERPREP AI ANALYSIS =====")
print("\nAI is analyzing... Please wait...\n")

process = subprocess.Popen(
    ["ollama", "run", "llama3.2"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    encoding="utf-8",
    errors="replace"
)

output, error = process.communicate(input=prompt)

print(output)

if error:
    print("\nOllama message:", error)