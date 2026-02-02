import pdfplumber
import json
import re
from groq import Groq
from core.settings import Api_key


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def analyze_resume_with_llm(resume_text, job_description):
    prompt = f"""
You are an AI assistant that analyzes resumes.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY valid JSON in this format:
{{
  "rank": 0-100,
  "skills": [],
  "total_experience": "",
  "project_category": []
}}
"""

    try:
        client = Groq(api_key=Api_key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content

        # extract JSON safely
        match = re.search(r"\{.*\}", raw, re.S)
        if not match:
            return {"error": "Invalid LLM response"}

        return json.loads(match.group())

    except Exception as e:
        return {
            "error": "LLM failed",
            "details": str(e)
        }


def process_resume(resume_path, job_description):
    resume_text = extract_text_from_pdf(resume_path)
    return analyze_resume_with_llm(resume_text, job_description)
