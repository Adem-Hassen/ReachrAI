import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
api_key=os.environ.get("API_KEY")

def create_model():
    model=ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=api_key)
    return model

