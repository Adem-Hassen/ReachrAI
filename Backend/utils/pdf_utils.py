import pdfplumber

def pdf_parser(file_path):
    exctracted_text=""
    if file_path:
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    exctracted_text+=page.extract_text() or ""
        except Exception as e:
            exctracted_text=f"error with parsing file {e}"
    return exctracted_text