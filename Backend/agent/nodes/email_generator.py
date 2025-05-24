from utils.message_generator import generate_message

def message_generator(state):
    resume_text=state.get("resume_txt")
    companies_matched=state.get("matched_companies")
    try:
        for company in companies_matched:
            message=generate_message(resume_text=resume_text,company_about=company.get("about"),company_link=company.get("link"))
            company["message_to_send"]=message
        return {**state,
                "matched_companies":companies_matched,
                "stage":"messages created"}
    
    except Exception as e:
        return {"error":e}

