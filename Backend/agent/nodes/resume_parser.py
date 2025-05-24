from utils.pdf_utils import pdf_parser


def resume_parser(state):
    resume_path=state.get("resume_file_path")
    resume_text=pdf_parser(resume_path)
    
    return {
        **state,
        "resume_text":resume_text.strip(),
        "stage": "parsed"
    }


