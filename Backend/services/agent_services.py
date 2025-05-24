from agent.flow import graph


def run_agent(resume_path):
    initial_state = {
        "resume_file_path":resume_path,
        "messages": [],
        "resume_txt": "",
        "matched_companies": [],
        "errors": [],
        "stage": "parse_resume"
    }
    result_state=graph.invoke(initial_state)
    companies=[company for company in result_state.get("matched_companies")]
    return {"companies":companies}
     