from utils.google_search import companies_search,extract_keywords

def match_companies(state):
    resumme_text=state.get("resume_txt")
    
    keywords=extract_keywords(resumme_text)
    print(keywords)
    matched_companies=companies_search(keywords=keywords,country="Tunisia")

    return {**state,
            "matched_companies":matched_companies,
            "stage":"matching"}
