from agent.model import create_model


def generate_message(resume_text,company_about,company_link):
    model=create_model()
    prompt=f"""You are an expert career advisor and email copywriter.
Your task is to write a professional cold outreach email (or LinkedIn message) from a job seeker to a company.
Use the following inputs:
1. Resume text: {resume_text}
2. Company description: {company_about}
3. Company linkedin link: {company_link}
Objectives:
- Write a cold email that introduces the candidate professionally.
- Highlight the most relevant skills and experiences from the resume that match the company’s work or values.
- Show enthusiasm and explain briefly why the candidate is a good fit.
- End with a polite and confident call to action (e.g., willingness to connect or provide more information).
Output format:
- Write in a polite, concise, and professional tone.
- Output only the email/message content — no extra commentary.
Now, generate the cold outreach email.
"""
    response=model.invoke(prompt)
    return(response.content)

